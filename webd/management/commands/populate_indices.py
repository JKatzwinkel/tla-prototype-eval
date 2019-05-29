import os
import json
from os import environ as env

from django.conf import settings
from django.core.files.storage import default_storage, FileSystemStorage
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk


es = Elasticsearch(
    env.get('ES_URL', 'http://localhost:9200')
)


class Indexer(object):
    def __init__(self, index):
        self.index = index
        self.queue = []
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
        if len(self.queue) > 100:
            self.bulk()

    def bulk(self):
        [
            res for res in streaming_bulk(
                es,
                self.queue,
                chunk_size=len(self.queue),
            )
        ]
        self.queue.clear()

    def __del__(self):
        self.bulk()


def index_folder_contents(path):
    """ """
    index = path.split(os.path.sep)[-1]
    print(index)
    indexer = Indexer(index)
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
