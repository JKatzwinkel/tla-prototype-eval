from setuptools import setup, find_packages

VERSION = "0.0.300"

setup(
        name='aaew-tla-lite',
        version=VERSION,
        packages=find_packages(),
        scripts=[
            'manage.py',
            ],
        install_requires=[
            "elasticsearch",
            "glom",
            "django",
            "django-extensions",
            ],
        )
