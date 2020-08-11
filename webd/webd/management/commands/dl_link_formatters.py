import os
import json
import yaml
import requests

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

TLA_CONF_URL = 'https://raw.githubusercontent.com/JKatzwinkel/tla-web/master/src/main/resources/application.yml'


def dl_tla_conf():
    return yaml.load_all(
        requests.get(
            TLA_CONF_URL
        ).content
    )


class Command(BaseCommand):
    help = 'Import link formatters from TLA web frontend repository'

    def extract_lf(self):
        for sec in dl_tla_conf():
            if 'tla' in sec:
                return sec['tla'].get('link-formatters')

    def handle(self, *args, **options):
        lf = self.extract_lf()
        with open(
            os.path.join(
                settings.MEDIA_ROOT,
                'link-formatters.json'
            ), 'w+'
        ) as f:
            json.dump(lf, f, indent=2)
