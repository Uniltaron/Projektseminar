# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: io.py 269 2008-06-13 19:46:40Z flarumbe $
#
# end: Platecom header

import dircache
import re
import pyThesaurus
from imp import find_module, load_module
from pyThesaurus.Thesaurus import Thesaurus
from StringIO import StringIO

def registerFormat(filetype, filehandler):
    _formats[filetype] = filehandler

def read(input, format, default_language, default_contexts=[], thesaurus=Thesaurus()):
	if not format in _formats:
		raise Exception, "Format %s not supported" % format
	if isinstance(input, str):
		input = StringIO(input)
	io = _formats[format](default_language,
			contexts=default_contexts,
			thesaurus=thesaurus)
	io.read(input)

def write(output, format, languages, contexts=[]):
	if not format in _formats:
		raise Exception, "Format %s not supported" % format
	if isinstance(input, str):
		output = StringIO(output)
	io = _formats[format](default_language, thesaurus=thesaurus,
			contexts=default_contexts)
	io.write(output)

def formats():
	return _formats.keys()

_formats = {}
import ioDing
import ioSKOSCore
"""
Cargo los formatos desde los modulos que comienzan con io, excepto io.
if _formats == None:
	_formats={}
	PATH=pyThesaurus.__path__
	iofile = re.compile("^io.+\.py$")
	for f in [ f for f in dircache.listdir(PATH[0]) if iofile.match(f) ]:
		name = f[0:-3]
		file, pathname, description = find_module(name, PATH)
		M = load_module(name, file, '', description)
"""
