# coding: utf-8

from setuptools import setup

setup(
    name='mkdocs-custom',
    version='0.1.0',
    description='mkdocs-custom',
    author='humangas',
    url='https://github.com/humangas/mkdocs-custom',
    packages=['mkdocs-custom'],
    include_package_data=True,
    install_requires=[
        'mkdocs>=0.15.3',
    ],
)

# mkdocs-custom, mkdocs 配下パス同じで置き換える。同じファイルが先にあれば削除する 
