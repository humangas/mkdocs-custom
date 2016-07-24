# coding: utf-8

"""

"""

from distutils.sysconfig import get_python_lib
import shutil, os, re


def get_contains_file_dirpaths(root_dir_path):
    """Return contains file dirpaths."""
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(root_dir_path)
            if len(filenames) > 0]


def copy_mkdocs_assets():
    """Copy mkdocs assts from mkdocs-custom."""
    root_dir_path = os.path.join(get_python_lib(), 'mkdocs-custom')
    copy_files_dirs = get_contains_file_dirpaths(root_dir_path)
    dst_root = os.path.join(os.path.dirname(root_dir_path), 'mkdocs')

    repattern = re.compile('\.py*')

    for dir in copy_files_dirs:
        dst = dir.replace(root_dir_path, dst_root)
        for rosource in os.listdir(dir):
            rosource_path = os.path.join(dir, rosource)
            if os.path.isfile(rosource_path) and not repattern.match(os.path.splitext(rosource_path)[1]):
                shutil.copy(rosource_path, dst)


if __name__ == '__main__':
    copy_mkdocs_assets()
