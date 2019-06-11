from os import environ as env
from django.core.management.base import BaseCommand, CommandError

from elasticsearch import Elasticsearch


es = Elasticsearch(
    env.get('ES_URL', 'http://localhost:9200')
)


class Command(BaseCommand):
    help = 'Removes sample corpus data indices from Elasticsearch Installation'

    def handle(self, *args, **options):
        for doc_type in [
            'wlist',
            'text',
            'occurrence',
            'annotation',
            'object',
            'sentence',
        ]:
            if es.indices.exists(doc_type):
                print(
                    'delete index {}.'.format(
                        doc_type,
                    )
                )
                es.indices.delete(
                    doc_type
                )
