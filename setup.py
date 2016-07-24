# coding: utf-8

from setuptools import setup

_NAME = 'mkdocs-custom'
_AUTHOR = 'humangas'

setup(
    name=_NAME,
    version='0.1.0',
    description='Copy mkdocs assts from mkdocs-custom.',
    author=_AUTHOR,
    url='https://github.com/{0}/{1}'.format(_AUTHOR, _NAME),
    packages=[_NAME],
    include_package_data=True,
    install_requires=[
        'mkdocs>=0.15.3',
    ],
    entry_points={
        'console_scripts': [
            'mkdocs-custom-install=cli:copy_mkdocs_assets',
        ],
    },
)
