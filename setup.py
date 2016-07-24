# coding: utf-8

from setuptools import setup

setup(
    name='mkdocs-custom',
    version='0.1.0',
    description='Copy mkdocs assts from mkdocs-custom.',
    author='humangas',
    url='https://github.com/humangas/mkdocs-custom',
    packages=['mkdocs-custom'],
    include_package_data=True,
    install_requires=[
        'mkdocs>=0.15.3',
    ],
)


from distutils.sysconfig import get_python_lib
import shutil, os

def get_contains_file_dirpaths(root_dir_path):
    """Return contains file dirpaths."""
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(root_dir_path)
            if len(filenames) > 0]

def copy_mkdocs_assets():
    """Copy mkdocs assts from mkdocs-custom."""
    root_dir_path = os.path.join(get_python_lib(), 'mkdocs-custom')
    copy_files_dirs = get_contains_file_dirpaths(root_dir_path)

    for dir in copy_files_dirs:
        dst = dir.replace('mkdocs-custom', 'mkdocs')
        for file in os.listdir(dir):
            shutil.copy(os.path.join(dir, file), dst)

copy_mkdocs_assets()
