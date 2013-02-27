# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: ioDing.py 269 2008-06-13 19:46:40Z flarumbe $
#
# end: Platecom header

import sys
from pyThesaurus.Thesaurus import Thesaurus
from pyThesaurus.Concept import Concept
from re import sub
import csv
import io

global Trace

def _simplify(s):
	s = sub('\s+', ' ', s)
	s = s.replace('\n','')
	return s.strip()

def _clean(s):
	s = sub(r'(\([^\)]*)', '', s)
	return s

class ding(csv.Dialect):
	delimiter=';'
	quotechar='"'
	doublequote=True
	skipinitialspace=True
	lineterminator='\r\n'
	escapechar='\\'
	quoting=csv.QUOTE_MINIMAL
csv.register_dialect("ding", ding)

class ioDing:
	"""

	""" 

	def __init__(self, language, contexts=[], thesaurus=Thesaurus()):
		self._t = thesaurus
		self._contexts = contexts
		self._dl = language

	def read(self, istream, encoding='utf-8'):
		class NoCommentsStream:
			""" Elimina los comentarios del archivo de entrada. """
			def __init__(self, stream):
				self.stream = stream
			def __iter__(self):
				return self
			def next(self):
				n = self.stream.next()
				return n.split("#")[0]
		reader = csv.reader(NoCommentsStream(istream), dialect='ding')
		for row in reader:
			c = Concept(et = [ u"%s@%s" % (unicode(_clean(t), encoding),self._dl) for t in row ], contexts=self._contexts) 
			self._t.append_concept(c)
		return None

	def write(self, ostream, encoding='utf-8'):
		writer = csv.writer(ostream, dialect='ding')
		ctls = [map(lambda s: s.split('@'), self._t[cid]['=']) for cid in self._t.concepts()]
		ts = [ [ t.decode(encoding) for t,l in tls if l == self._dl ] for tls in ctls ]
		writer.writerows(ts)
		return None

	def thesaurus(self):
		return self._t

io.registerFormat('Ding', ioDing)
