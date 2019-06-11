import os
import json
from os import environ as env

from django.conf import settings
from django.core.files.storage import default_storage, FileSystemStorage
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk, BulkIndexError


es = Elasticsearch(
    env.get('ES_URL', 'http://localhost:9200')
)


def put_field_value(obj, field_path, field_value):
    """ makes sure that within the object, the field specified by its path
    has the specified value.
    """
    element = obj
    segments = field_path.split('.')
    for segment in segments[:-1]:
        if segment not in element:
            element[segment] = {}
        element = element[segment]
    element[segments[-1]] = field_value


class Indexer(object):
    def __init__(self, index, path):
        self.index = index
        self.queue = []
        self.path = path
        self.fail = False
        print(
            'create indexer for index {} at ES instance {} '.format(
                index,
                env.get('ES_URL'),
            )
        )
        if not es.indices.exists(index):
            es.indices.create(index)

    def add(self, doc):
        self.queue.append(
            {
                "_op_type": "index",
                "_index": self.index,
                "_type": self.index,
                "_id": doc.get("id"),
                "_source": doc,
            }
        )
        if len(self.queue) > 100 and not self.fail:
            self.bulk()


    def bulk(self):
        try:
            [
                res for res in streaming_bulk(
                    es,
                    self.queue,
                    chunk_size=len(self.queue),
                )
            ]
            self.clear_queue()
            return True
        except BulkIndexError as e:
            print(
                'error during population of {} index!'.format(
                    self.index,
                )
            )
            self.fail = True
            self.fix_index()
            return False

    def fix_index(self):
        settings = es.indices.get_settings(
            index=self.index
        )
        settings_path = '{}.settings.index.block.read_only_allow_delete'.format(
            self.index
        )
        put_field_value(
            settings,
            settings_path,
            'false'
        )
        try:
            es.indices.put_settings(
                settings,
                index=self.index
            )
            self.fail = False
        except:
            pass


    def clear_queue(self):
        while len(self.queue) > 0:
            action = self.queue.pop()
            i = action.get('_id')
            fn = os.path.join(
                self.path,
                '{}.json'.format(
                    i
                )
            )
            if os.path.exists(fn):
                os.remove(fn)

    def __del__(self):
        self.bulk()


def index_folder_contents(path):
    """ """
    index = path.split(os.path.sep)[-1]
    indexer = Indexer(
        index,
        os.path.join(
            settings.MEDIA_ROOT,
            path
        )
    )
    for fn in os.listdir(
        os.path.join(
            settings.MEDIA_ROOT,
            path
        )
    ):
        doc = json.loads(
            default_storage.open(
                os.path.join(path, fn)
            ).read().decode(
                'utf8'
            )
        )
        indexer.add(doc)
    indexer.bulk()


class Command(BaseCommand):
    help = 'Populates the Elasticsearch instance at $ES_URL'

    def handle(self, *args, **options):
        for doc_type in [
            'wlist',
            'text',
            'occurrence',
            'annotation',
            'object',
            'sentence',
        ]:
            index_folder_contents(
                os.path.join(
                    'corpus',
                    'sample',
                    doc_type
                )
            )
