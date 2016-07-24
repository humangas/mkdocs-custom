# coding: utf-8

from setuptools import setup


setup(
    name='mkdocs_custom',
    version='0.1.0',
    description='Copy mkdocs assts from mkdocs-custom.',
    author='humangas',
    url='https://github.com/humangas/mkdocs-custom',
    packages=['mkdocs_custom'],
    include_package_data=True,
    install_requires=[
        'click',
        'mkdocs>=0.15.3',
    ],
    entry_points={
        'console_scripts': [
            'mkdocs-custom = mkdocs_custom.cli:mkdocs_custom',
        ],
    },
)
