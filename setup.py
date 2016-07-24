# coding: utf-8

from setuptools import setup
from distutils.sysconfig import get_python_lib
from distutils.command.install import install as _install
import os, sys, shutil

MODULE_NAME = 'mkdocs-custom'

def _post_install(dir):
    from subprocess import call
    call([sys.executable, 'cli.py'], cwd=os.path.join(dir, MODULE_NAME))


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")


setup(
    name=MODULE_NAME,
    version='0.1.0',
    description='Copy mkdocs assts from mkdocs-custom.',
    author='humangas',
    url='https://github.com/humangas/'.format(MODULE_NAME),
    packages=[MODULE_NAME],
    include_package_data=True,
    install_requires=[
        'mkdocs>=0.15.3',
    ],
    entry_points={
        'console_scripts': [
            'mkdocs-custom-install=cli:copy_mkdocs_assets',
        ],
    },
    cmdclass={'install': install},
)
