#!/usr/bin/env python

from setuptools import setup

__version__ = '0.0.1'

setup(
  name='chrome-pass',
  version=__version__,
  author='Dmytro Sadovnychyi',
  author_email='pip@dmit.ro',
  url='https://github.com/sadovnychyi/chrome-passwords-cli',
  description='Access your Chrome passwords from CLI.',
  scripts=['pass.py'],
  keywords='chrome password',
  license='MIT',
  install_requires=[
    'pycryptodome',
    'keyring >= 13.2.1'
  ]
)
