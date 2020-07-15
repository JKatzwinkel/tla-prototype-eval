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
        "elasticsearch>=7.0.0",
        "glom>=19.2.0",
        "django",
        "django-extensions",
        "aaew-linggloss @ git+https://github.com/JKatzwinkel/aaew-linggloss.git@master",
    ],
)
