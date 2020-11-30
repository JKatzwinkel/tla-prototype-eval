from setuptools import setup, find_packages

VERSION = "0.1.0"

setup(
    name='tla-prototype',
    version=VERSION,
    packages=find_packages(),
    scripts=[
        'manage.py',
    ],
    install_requires=[
        "elasticsearch>=7.7.1",
        "glom>=19.2.0",
        "requests",
        "pyyaml",
        "django",
        "django-extensions",
        "aaew-linggloss @ git+https://github.com/dwerning/aaew-linggloss.git@master",
    ],
)
