import os
from os import environ as env

from django.conf import settings
from django.core.files.storage import default_storage, FileSystemStorage
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk


es = Elasticsearch(
    env.get('ES_URL')
)


class Indexer(object):
    def __init__(self, index):
        self.index = index
        self.cache = []

    def index(self, doc):
        self.cache.append(
            {
                "_op_type": "index",
                "_index": self.index,
                "_type": self.index,
                "_id": doc.get('_id'),
                '_source': doc,
            }
        )
        if len(self.cache) > 100:
            self.bulk()

    def bulk(self):
        streaming_bulk(
            es,
            self.cache,
            chunk_size=len(self.cache),
        )
        self.cache.clear()

    def __del__(self):
        self.bulk()


def index_folder_contents(path):
    """ """
    for fn in os.listdir(
        os.path.join(
            settings.MEDIA_ROOT,
            path
        )
    ):
        doc = default_storage.open(
            os.path.join(path, fn)
        ).read()
        print(doc.get('_id'))


class Command(BaseCommand):
    help = 'Populates the Elasticsearch instance at $ES_URL'

    def handle(self, *args, **options):
        print(
            default_storage.exists('test.json')
        )
        for path in [
            'wlist',
            'text',
            'occurrence',
        ]:
            index_folder_contents(
                os.path.join(
                    'download',
                    path
                )
            )
