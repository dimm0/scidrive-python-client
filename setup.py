#!/usr/bin/env python
import os
import subprocess
import shutil
import sys

from setuptools import setup, find_packages

parent_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

INSTALL_REQUIRES = ['config', 'argparse']
if sys.version_info < (2, 6):
    INSTALL_REQUIRES.append('simplejson') # The 'json' module is included with Python 2.6+

setup(name='vobox-python-client',
      version='0.1.0',
      description='VOBox REST API Client',
      author='Dmitry Mishin',
      author_email='dmitry@pha.jhu.edu',
      url='http://usvao.org',
      scripts=['bin/vobox'],
      packages=['dropbox', 'tests'],
      install_requires=INSTALL_REQUIRES,
      long_description=open('./README.md').read(),
     )
