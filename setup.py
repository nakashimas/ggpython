# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
from importlib import resources

# =============================================================================> 
# readme
with open('README.md', encoding = 'utf-8') as f:
    README = f.read().replace("\r", "")

# =============================================================================> 
# license
with open('LICENSE', encoding = 'utf-8') as f:
    LICENSE = f.read()

# =============================================================================> 
# requires
print("--------------------")
with open('requirements.txt', encoding = 'utf-8') as f:
    REQUIRES = []
    require = f.readline()
    while require:
        print(require)
        REQUIRES.append(require)
        require = f.readline()
print("--------------------")

# =============================================================================> 
# package data
PACKAGE_DATA = {}

# =============================================================================> 
# author
AUTHOR = "nakashimas"
AUTHOR_EMAIL = "nascor.neco@gmail.com"

# =============================================================================> 
# description
DESCRIPTION = "Tracker Network Wrapper In Python."

# =============================================================================> 
# version
VERSION = "0.0.0"

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10'
]

# =============================================================================> 
setup(
    name = 'ggpython',
    keywords = '',
    version = VERSION,
    description = DESCRIPTION,
    long_description = README,
    long_description_content_type = "text/markdown",
    license = LICENSE,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = 'https://github.com/nakashimas/ggpython',
    packages = find_packages(exclude = ('tests', 'docs', 'dest', 'dist')),
    package_data = PACKAGE_DATA,
    install_requires = REQUIRES,
    classifiers = CLASSIFIERS,
    include_package_data = True,
    test_suite = 'tests'
)
