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
            "elasticsearch>=6.0.0,<7.0.0",
            "glom>=19.2.0",
            "django",
            "django-extensions",
            ],
        )
