# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: ioSKOSCore.py 269 2008-06-13 19:46:40Z flarumbe $
#
# end: Platecom header

import sys
from xml.sax import parse, parseString
from xml.sax import SAXNotRecognizedException, SAXNotSupportedException
from xml.sax.saxutils import XMLGenerator
from xml.sax.handler import ContentHandler
from xml.sax.xmlreader import AttributesNSImpl
from pyThesaurus.Thesaurus import Thesaurus
from pyThesaurus.Concept import Concept
from re import sub
import io

global Trace

def _simplify(s):
	s = sub('\s+', ' ', s)
	s = s.replace('\n','')
	return s.strip()

class SkosCoreHandler(ContentHandler):
	"""
	Clase que maneja la interpretaciÃn del RDF
	"""
	_ignored_tags = [ 'skos:subjectindicator', 'dc:description' ] 

	def warning(self, err):
		import sys
		sys.stderr.write("\nWarning: %s\n" % err)

	def error(self, err):
		import sys
		sys.stderr.write("\nERROR: %s\n" % err)
		raise Exception

	def _label(self, label):
		"""
		"""
		if not self._lang:
			return "%s@%s" % (self._data, self._dl)
		else:
			return "%s@%s" % (self._data, self._lang)
	
	def _get_concept(self, cid):
		"""
		"""
		if not cid in self._concepts:
			raise Exception, "No term for concept %s" % cid
		return self._concepts[cid]

	def __init__(self, dl, t=Thesaurus(), schemes=[]):
		"""
		"""
		self._dl = dl
		self._t = None
		self._labels = []
		self._hlabels = []
		self._data = ''
		self._lang = None
		self._broader = None
		self._narrower = None
		self._about = None
		self._concepts = None
		self._to_broader = None
		self._to_narrower = None
		self._to_related = None
		self._pubn = None
		self._privn = None
		self._dict = None
		self._dict_path = None
		self._schemes = None
		self._default_schemes = schemes
		self._t = t
		self._i = 0

	def startElement(self, name, attributes):
		"""
		"""
		name = name.lower()
		if name=="rdf:rdf":
			self._concepts = {}
			self._to_broader = {}
			self._to_narrower = {}
			self._to_related = {}
			pass
		elif name=="skos:concept":
			self._labels = []
			self._hlabels = []
			self._data = ''
			self._lang = None
			self._broader = None
			self._narrower = None
			self._about = attributes.get('rdf:about')
			self._pubn = {}
			self._privn = {}
			self._schemes = self._default_schemes
		elif name in [ "skos:preflabel", "skos:altlabel",
				"skos:hiddenlabel", "skos:collection",
				"skos:definition" ]:
			self._data = ""
			self._lang = attributes.get('xml:lang')
		elif name=="skos:broader":
			if not self._about in self._to_broader:
				self._to_broader[self._about] = []
			self._to_broader[self._about].append(attributes.get('rdf:resource'))
		elif name=="skos:narrower":
			if not self._about in self._to_narrower:
				self._to_narrower[self._about] = []
			self._to_narrower[self._about].append(attributes.get('rdf:resource'))
		elif name=="skos:related":
			if not self._about in self._to_related:
				self._to_related[self._about] = []
			self._to_related[self._about].append(attributes.get('rdf:resource'))
		elif name=="skos:changenote":
			self._dict = {}
			self._dict_path = [ self._dict ]
		elif name=="dc:creator":
			self._dict_path[-1]['creator'] = {}
			self._dict_path.append(self._dict_path[-1]['creator'])
		elif name=="foaf:person":
			self._dict_path[-1]['person'] = {}
			self._dict_path.append(self._dict_path[-1]['person'])
		elif name=="dcterm:rfc1766":
			self._dict_path[-1]['rfc1766'] = {}
			self._dict_path.append(self._dict_path[-1]['rfc1766'])
		elif name=="dc:language":
			self._dict_path[-1]['language'] = {}
			self._dict_path.append(self._dict_path[-1]['language'])
		elif name=="foaf:document":
			self._dict_path[-1]['document'] = {}
			self._dict_path.append(self._dict_path[-1]['document'])
			if attributes.get('rdf:resource'): self._dict_path[-1]['resource'] = attributes.get('rdf:resource')
		elif name=="foaf:mbox":
			self._dict_path[-1]['mbox'] = attributes.get('rdf:resource')
		elif name=="skos:scopenote":
			self._dict = {}
			if attributes.get('rdf:resource'): self._dict['resource'] = attributes.get('rdf:resource')
			self._dict_path = [ self._dict ]
		elif name=="skos:inscheme":
			if attributes.get('rdf:resource'): self._schemes.append(attributes.get('rdf:resource'))
		elif name in ['rdf:value', 'skos:prefsymbol', 'foaf:name', 'dc:date',
					 'skos:altsymbol', 'dcterms:rfc1766', 'rdfs:label',
			] + SkosCoreHandler._ignored_tags:
			pass
		else:
			raise SAXNotRecognizedException("<%s>" % name)

	def _concept_list_(self, f, map):
		"""
		"""
		l = [ (self._concepts[_c], self._t[self._concepts[_i]]['='])
				for _c, _l in map.items()	if _c in self._concepts
				for _i in _l				if _i in self._concepts
				]
		for c, i in l:
			for t in i:
				f(c).append(t)
	
	def endElement(self, name):
		"""
		"""
		name = name.lower()
		if name=="rdf:rdf":
			self._concept_list_(lambda i: self._t[i]._bt, self._to_broader)
			self._concept_list_(lambda i: self._t[i]._nt, self._to_narrower)
			self._concept_list_(lambda i: self._t[i]._rt, self._to_related)
			pass
		elif name=="skos:concept":
			c = Concept(et = self._labels, ht = self._hlabels, pubn=self._pubn, contexts=self._schemes)
			self._concepts[self._about] = self._t.append_concept(c)
		elif name=="skos:preflabel":
			self._labels = [ self._label(self._data) ] + self._labels
		elif name=="skos:altlabel":
			self._labels.append(self._label(self._data))
		elif name=="skos:hiddenlabel":
			self._hlabels.append(self._label(self._data))
		elif name=="skos:collection":
			self._data = ""
		elif name=="skos:definition":
			if not 'definition' in self._pubn: self._pubn['definition'] = []
			self._pubn['definition'].append(self._label(self._data))
		elif name=="skos:changenote":
			if not 'changenote' in self._pubn: self._pubn['changenote'] = []
			self._pubn['changenote'].append(self._dict)
		elif name=="rdf:value":
			self._dict_path[-1]['value'] = _simplify(self._data)
		elif name=="foaf:name":
			self._dict_path[-1]['name'] = _simplify(self._data)
		elif name=="rdfs:label":
			self._dict_path[-1]['label'] = _simplify(self._data)
		elif name in [ "dc:creator", "foaf:person", "dcterms:rfc1766",
				"dc:language", "foaf:document" ]:
			self._dict_path = self._dict_path[:-1]
		elif name=="skos:scopenote":
			if not 'scopenote' in self._pubn: self._pubn['scopenote'] = []
			self._pubn['scopenote'].append(self._dict)
		elif name in [ 'skos:broader', 'skos:narrower', 'skos:prefsymbol',
				'skos:related', 'foaf:mbox', 'skos:altsymbol', 'dc:date',
				'skos:inscheme' 
			] + SkosCoreHandler._ignored_tags:
			pass
		else:
			raise SAXNotRecognizedException("</%s>" % name)
		self._data = ''
		self._lang = None

	def characters(self, ch):
		"""
		"""
		self._data += ch

	def Thesauri(self):
		"""
		"""
		return self._t

class SkosCoreWriter:
	xmlns = {
			'rdf':	u'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
			'rdfs':	u'http://www.w3.org/2000/01/rdf-schema#',
			'skos':	u'http://www.w3.org/2004/02/skos/core#',
			'xml':	u'http://www.w3.org/XML/1998/namespace',
			'foaf':	u'http://xmlns.com/foaf/0.1/',
			'dc':	u'http://purl.org/dc/elements/1.1/',
			'dcterms':	u'http://purl.org/dc/terms/',
			}

	def __init__(self, output, encoding='utf-8', source='http://platecom.inter-cultura.com/concepts', lang=['en','es','fr','de','nl']):
		self._l = lang
		self._term_url = lambda t: "%s#%s" % (source, t)
		self._concept_url = lambda c: self._term_url(c.get_prefered(self._l)[0])
		self._xml = XMLGenerator(output, encoding)
		self._xml.startDocument()
		for prefix, uri in self.xmlns.items():
			self._xml.startPrefixMapping(prefix or None, uri)
		pass

	def close(self):
		self._xml.endDocument()
		return

	def _build_tag(self, tag):
		if type(tag) == type(""):
			qname = tag
			tag = (None, tag)
		else:
			qname = "%s:%s" % tag
			tag = (self.xmlns[tag[0]], tag[1])
		return tag, qname

	def startNode(self, tag, attr={}):
		tag, qname = self._build_tag(tag)
		self._xml.startElementNS(tag, qname, attr)
	
	def endNode(self, tag):
		tag, qname = self._build_tag(tag)
		self._xml.endElementNS(tag, qname)
	
	def simpleNode(self, tag, value, attr={}):
		self.startNode(tag, attr)
		if value: self._xml.characters(value)
		self.endNode(tag)

	def writeThesaurus(self, t):
		self.startNode(('rdf', 'RDF'), {})

		for c in t.concepts():
			self.writeConcept(t[c])

		self.endNode(('rdf', 'RDF'))

	def writeConcept(self, c):
		if c.get_prefered(self._l) == []: return # No escribo conceptos sin términos
		attr={ (self.xmlns['rdf'],'about'): self._concept_url(c) }
		self.startNode(('skos', 'Concept'), attr)
		pt = c.get_prefered(self._l[0])
		for tl in c['=']:
			t, l = tl.split("@")
			attr={ (self.xmlns['xml'],'lang'): l }
			if tl in pt:
				self.simpleNode(('skos', 'prefLabel'), t, attr)
			else:
				self.simpleNode(('skos', 'altLabel'), t, attr)
		for tl in c['#']:
			t, l = tl.split("@")
			attr={ (self.xmlns['xml'],'lang'): l }
			self.simpleNode(('skos', 'hiddenLabel'), t, attr)
		for tl in c['<']:
			resource = self._term_url(tl)
			attr={ (self.xmlns['rdf'],'resource'): resource }
			self.simpleNode(('skos', 'broader'), t, attr)
		for tl in c['>']:
			resource = self._term_url(tl)
			attr={ (self.xmlns['rdf'],'resource'): resource }
			self.simpleNode(('skos', 'narrower'), t, attr)
		for tl in c['-']:
			resource = self._term_url(tl)
			attr={ (self.xmlns['rdf'],'resource'): resource }
			self.simpleNode(('skos', 'related'), t, attr)
		for tl in c['~']:
			self.warning('SKOS not support similar concepts')

		self.writePublicNotes(c._pubn.items())

		self.endNode(('skos', 'Concept'))
		pass

	def writePublicNotes(self, n):
		for k,v in n:
			if k == 'definition':
				for i in v:
					value, lang = i.split('@')
					attr={ (self.xmlns['xml'],'lang'): lang }
					self.simpleNode(('skos', 'definition'), value, attr)
			if k == 'changenote':
				for i in v:
					attr={ (self.xmlns['rdf'],'parseType'): 'Resource' }
					self.startNode(('skos', 'changenote'), attr)
					if 'value' in i: self.simpleNode(('rdf', 'value'), i['value'], {})
					if 'creator' in i:
						self.writeCreator(i['creator'])
					self.endNode(('skos', 'changenote'))
			if k == 'scopenote':
				for i in v:
					attr = {}
					if 'resource' in  i and i['resource'] != None: attr[(self.xmlns['rdf'],'resource')] = i['resource']
					self.startNode(('skos', 'scopenote'), attr)
					if 'document' in i: self.writeDocument(i['document'])
					self.endNode(('skos', 'scopenote'))

	def writeDocument(self, d):
		attr = {}
		if 'resource' in  d and d['resource'] != None: attr[(self.xmlns['rdf'],'resource')] = d['resource']
		self.startNode(('foaf', 'document'), attr)
		if 'creator' in d:  self.writeCreator(d['creator'])
		if 'language' in d: self.writeLanguage(d['language'])
		self.endNode(('foaf', 'document'))

	def writeLanguage(self, l):
		self.startNode(('dc', 'language'), {})
		self.startNode(('dcterms', 'RFC1766'), {})
		self.simpleNode(('rdf', 'value'), l['value'] , {})
		self.simpleNode(('rdfs', 'label'), l['label'] , {})
		self.endNode(('dcterms', 'RFC1766'))
		self.endNode(('dc', 'language'))

	def writeCreator(self, c):
		self.startNode(('dc', 'creator'), {})
		if 'person' in c:
			self.startNode(('foaf', 'person'), {})
			if 'name' in c['person']:
				self.simpleNode(('foaf', 'name'), c['person']['name'], {})
			if 'mbox' in c['person']:
				attr={ (self.xmlns['rdf'],'resource'): c['person']['mbox'] }
				self.simpleNode(('foaf', 'mbox'), None, attr)
			self.endNode(('foaf', 'person'))
		self.endNode(('dc', 'creator'))

def load(file, dl, default_context=None):
	"""
	load([file|str], str) -> Thesauri

	Load a thesauri in SKOS-Core format from a file or string. If term have no language is defined as dl
	"""
	skosCoreHandler = SkosCoreHandler(dl)
	if isinstance(file, str):
		parseString(file, skosCoreHandler)
	else:
		parse(file, skosCoreHandler)
	return skosCoreHandler.Thesauri()

def save(file, thesauri, default_context=None):
	"""
	save(file, Thesauri) -> None

	Store a thesauri in SKOS-Core format in a file.
	"""
	W = SkosCoreWriter(file)
	W.writeThesaurus(thesauri)

def write_concepts(file, concepts):
	"""
	write_concepts(file, concept) -> None

	Write a list of concepts in SKOS-Core format in a file.
	"""
	W = SkosCoreWriter(file)
	W.startNode(('rdf', 'RDF'), {})
	for c in concepts:
		W.writeConcept(c)
	W.endNode(('rdf', 'RDF'))

class ioSKOSCore:
	def __init__(self, language, contexts=[], thesaurus=Thesaurus()):
		self._t = thesaurus
		self._contexts = contexts
		self._dl = language

	def read(self, istream, encoding=None):
		skosCoreHandler = SkosCoreHandler(self._dl, schemes=self._contexts, t=self._t)
		parse(istream, skosCoreHandler)
		return None

	def write(self, ostream, encoding=None):
		W = SkosCoreWriter(ostream)
		W.writeThesaurus(self._t)
		return None

	def thesaurus(self):
		return self._t

io.registerFormat('SKOSCore', ioSKOSCore)
