# coding: utf-8

from __future__ import print_function
from distutils.sysconfig import get_python_lib
import shutil, os, re
import click


@click.group()
def mkdocs_custom():
    """
    It is a tool for expanding the mkdocs.

    See also:
        - mkdocs: https://github.com/mkdocs/mkdocs/
        - mkdocs-custom: https://github.com/humangas/mkdocs-custom
    """
    pass


@mkdocs_custom.command()
def install():
    """
    After all ..., copy mkdocs assts from mkdocs-custom/*.

    The following is extended.

    - Japanese search correspondence
    """
    _copy_mkdocs_assets()


def _get_contains_file_dirpaths(root_dir_path):
    """Return contains file dirpaths."""
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(root_dir_path)
            if len(filenames) > 0]


def _copy_mkdocs_assets():
    """Copy mkdocs assts from mkdocs_custom."""
    root_dir_path = os.path.join(get_python_lib(), 'mkdocs_custom')
    copy_files_dirs = _get_contains_file_dirpaths(root_dir_path)
    dst_root = os.path.join(os.path.dirname(root_dir_path), 'mkdocs')
    repattern = re.compile('\.py*')

    for dir in copy_files_dirs:
        dst = dir.replace(root_dir_path, dst_root)
        for rosource in os.listdir(dir):
            rosource_path = os.path.join(dir, rosource)
            if os.path.isfile(rosource_path) and not repattern.match(os.path.splitext(rosource_path)[1]):
                print('Copy: {0} -> {1}'.format(rosource_path, dst))
                shutil.copy(rosource_path, dst)

    print('Successfully Complete: install')


if __name__ == '__main__':
    mkdocs_custom()
