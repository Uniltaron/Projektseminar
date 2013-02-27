# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: setup.py 370 2008-10-06 16:48:00Z mromero $
#
# end: Platecom header
"""Distutils setup file, used to install or test 'pyThesaurus'"""

import os
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

source_path=os.path.join(os.path.dirname(__file__), 'pyThesaurus')
version=open(os.path.join(source_path, 'version.txt')).read()
long_description=open(os.path.join(source_path, 'README.txt')).read() + '\n\n'

setup(
	name='pyThesaurus',
	version=version,
	description='Ontology module with Thesaurus administration model. Developed for Platecom project.',
	long_description=long_description,
	license="GPL",
	classifiers=[
	"Topic :: Software Development :: Libraries :: Python Modules",
	"Environment :: No Input/Output (Daemon)",
	"Framework :: Buildout",
	"Intended Audience :: Information Technology",
	"License :: OSI Approved :: GNU General Public License (GPL)",
	"Operating System :: OS Independent",
	"Programming Language :: Python",
	],
	keywords='platecom, thesaurus, thesauri, ontology',
	author='Inter-Cultura Consultora SRL - Ibai Sistemas SA - Eusko Ikaskuntza-Sociedad de Estudios Vascos',
	author_email='dev@inter-cultura.com',
	url='http://www.platecom.com/productos/pythesaurus/',
	packages=find_packages(),
	package_data={},
	install_requires=[],
	test_suite="pyThesaurus.tests",
)

