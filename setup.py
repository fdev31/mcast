#!/usr/bin/env python

import codecs
from setuptools import setup

version = [line.split('=')[1].strip() for line in open('mcast').readlines() if line.startswith('__version__')][0].strip('"')

setup(
    name = "mcast",
    description = 'Python Multicast file transfer CLI tool - also comes with nc/netcat implementation',
    version = version,
    url = 'https://github.com/fdev31/mcast',
    author = 'Fabien Devaux',
    author_email = 'fdev31@gmail.com',
    scripts = ['mcast', 'nc.py'],
    license = "BSD",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    long_description = codecs.open('README.rst', encoding='utf-8').read(),
)
