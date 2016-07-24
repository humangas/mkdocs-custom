# coding: utf-8

from setuptools import setup

setup(
    name='mkdocs-custom',
    version='0.1.0',
    description='mkdocs-custom',
    author='humangas',
    url='https://github.com/humangas/mkdocs-custom',
    packages=['mkdocs'],
    include_package_data=True,
    install_requires=[
        'mkdocs>=0.15.3',
    ],
)
