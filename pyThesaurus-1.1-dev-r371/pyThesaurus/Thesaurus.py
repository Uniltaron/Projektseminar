# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: Thesaurus.py 361 2008-07-31 22:07:50Z flarumbe $
#
# end: Platecom header

from config import *
from Concept import Concept

def _join_(self, s, l=[]):
	"""
	_join_(object, str, list<str>) -> list<str>

	Get a list of terms@lang in supported languages
	"""
	return [ "%s@%s" % (s, i) for i in l if l in self._lang ]

def _split_(self, s):
	"""
	_split_(object, str) -> str, str

	Separe the term and the language from the string
	"""
	return s.split("@")

class Thesaurus:
	def __init__(self, lang=[], TDict=dict, TList=list):
	   """
	   __init__(object) -> Thesurus

	   Init the Thesaurus.
	   """
	   self._dict = TDict
	   self._list = TList
	   self._concept = self._dict()
	   self._term = self._dict()
	   self._context = self._dict()
	   self._last_concept_id = -1 
	   self._lang = self._list()

	def get_prefered(self, t, lang=[], contexts=None):
		"""
		get_prefered(object, str, list<str>) -> list<str>

		Return prefered terms of term t in all languages in lang. If lang is [] return all terms.
		"""
		cs = self(t, contexts)

		ts = []

		for c in cs:
		  ts += self._concept[c].get_prefered(lang)

		return ts

	def set_prefered(self, t, cid):
		"""
		set_prefered(object, str, cid) -> None

		Set the prefered term t in some language in concept cid
		"""
		self._concept[cid].set_prefered(t)

	def get_equivalent(self, t, lang=[], contexts=None, exclude = False):
		"""
		get_equivalent(object, str, list<str>) -> list<str>

		Return equivalent terms of term t in all languages in lang. If lang is [] return all terms.
		"""
		cid = self(t, contexts)

		ts = []
		for c in cid:
			ts += self[c]['=']

		ts = dict([ ("%s@%s" % (_t,_l), None) for _t,_l in [ t_.split('@') for t_ in ts ] if _l in lang ]).keys()

		if exclude and t in ts:
			ts.remove(t)

		return ts

	def get_similars(self, t, lang=[], contexts=None):
		"""
		get_similars(object, str, list<str>) -> list<str>

		Return similar terms of term t in all languages in lang. If lang is [] return all terms.
		"""
		cid = self(t, contexts)

		ts = []
		for c in cid:
			ts += self[c]['~']

		ts = dict([ ("%s@%s" % (t,l), None) for t,l in [ t.split('@') for t in ts ] if l in lang ]).keys()

		return ts

	def get_broader(self, t, lang=[], contexts=None):
		"""
		get_broader(object, str, list<str>) -> list<str>

		Return broaders terms of term t in all languages in lang. If lang is [] return all terms.
		"""
		cid = self(t, contexts)

		ts = []
		for c in cid:
			ts += self[c]['<']

		ts = dict([ ("%s@%s" % (t,l), None) for t,l in [ t.split('@') for t in ts ] if l in lang ]).keys()

		return ts

	def get_narrower(self, t, lang=[], contexts=None):
		"""
		get_narrower(object, str, list<str>) -> list<str>

		Return narrower terms of term t in all languages in lang. If lang is [] return all terms.
		"""
		cid = self(t, contexts)

		ts = []
		for c in cid:
			ts += self[c]['>']

		ts = dict([ ("%s@%s" % (t,l), None) for t,l in [ t.split('@') for t in ts ] if l in lang ]).keys()

		return ts

	def get_related(self, t, lang=[], exclude=True, contexts=None):
		"""
		get_related(object, str, list<str>) -> list<str>

		Return related terms of term t in all languages in lang. If lang is [] return all terms.
		"""
		cid = self(t, contexts)

		ts = []
		hidden = False
		for c in cid:
			ts += self[c]['-']
			hidden = hidden or t in self[c]['#']

		ts = dict([ ("%s@%s" % (_t,_l), None) for _t,_l in [ t_.split('@') for t_ in ts ] if _l in lang ]).keys()

		if exclude or hidden:
			return ts
		else:
			return ts + [ t ]

	def get_concepts(self, ts, contexts=None):
		"""
		get_concepts(object, list<str>) -> int

		Return the concepts id associated to all terms in ts.
		"""
		cid = []
		for t in ts:
			cid += self(t, contexts)

		return dict([ (c, None) for c in cid ]).keys()

	def get_publicNotes(self, c):
		"""
		get_publicNotes(object, int) -> dict

		Return the dict of public notes of a concept.

		get_publicNotes(c).keys() =	[ 'definition', 'scopeNote', 'example', 'historyNote', 'class' ]
		get_publicNotes(c)[x].keys() = [ 'value', 'date', 'creator' ]
		"""
		return self[c]._pubn

	def get_privateNotes(self, c):
		"""
		get_privateNotes(object, int) -> dict

		Return the dict of private notes of a concept.

		get_privateNotes(c).keys() = [ 'editorialNote', 'changeNote' ]
		get_privateNotes(c)[x].keys() = [ 'value', 'date', 'creator' ]
		"""
		return self[c]._privn

	def terms(self, contexts=None):
		"""
		terms(object) -> list<str>

		Return the list of terms of the thesauro
		"""
		return self._term.keys()

	def concepts(self, contexts=None):
		"""
		terms(object) -> list[int]

		Return the list of concepts id of the thesaurus
		"""
		return self._concept.keys()

	def concepts_objects(self, contexts=None):
		"""
		terms(object) -> list[object]

		Return the list of concepts of the thesaurus
		"""
		return self._concept.values()

	def contexts(self):
		"""
		contexts(object) -> list<str>

		Return a list of classes.
		"""
		return self._context.keys()

	def search_term(self, str, contexts=None):
		"""
		search_term(str) -> list<str>

		Return a list of similar terms to the str
		"""
		import re
		cre = re.compile(str)

		return [ k for k in self._term.keys() if cre.search(k) ]

	def __getitem__(self, idx):
		"""
		__getitem__(object, int) -> dict

		Return the concept dict of idx.

		__getitem__(idx).keys() = [ '=', '#', '<', '>', '-', '~', concept_id... ] 
		if c not defined(object, raise IndexError, 'not defined'
		"""
		if idx in self._concept:
		   return self._concept[idx]
		else:
		   raise IndexError, 'not defined'

	def __call__(self, t, contexts=None):
		"""
		__call__(object, str, list<string>) -> list<int>

		Return the concept id of the term.

		if t not defined(object, raise IndexError, 'not defined'
		"""
		if t in self._term:
			return [ cid for cid in self._term[t] if self.in_contexts(cid, contexts) ]
		else:
			raise IndexError, 'not defined'
	
	def in_contexts(self, cid, contexts):
		return contexts==None or contexts==[] or sum([ xc==xi for xc in self._concept[cid]._contexts for xi in contexts ])

	def exist_term(self, t, contexts=None):
		"""
		exist_term(object, str, list<string>) -> list<int>

		Return true if t is defined in contexts.
		"""
		return t in self._term and len(self(t, contexts)) > 0

	def append_term(self, t, et=[], ht=[], net=[], bt=[], nt=[], rt=[], st=[], contexts=None, automatic=False):
		"""
		append_term(object, str, int, et=list<str>, ht=list<str>, net=list<str>, bt=list<str>,
							 nt=list<str>, rt=list<str>,  st=list<str>, automatic=bool,
							 contexts=list<str>) -> None

		Add a new term t of class c with the following relations.
		"""
		append_concept_id = Concept(et=[t] + et, ht=ht, net=net, bt=bt, nt=nt, st=st, rt=rt, contexts=contexts)
		old_concept_at = self._previous_concept_to_join(append_concept_id)
		if old_concept_at is None:
			self.append_concept(append_concept_id)
		elif automatic:
			self.replace_concept_at(self[old_concept_at].join_to(append_concept_id), old_concept_at)
		else:
			raise ConceptsConflict, t

	def _previous_concept_to_join(self, append_concept, M=matrix_comparation, S=minimum_score):
		"""
		_previous_concept_to_join(object, Concept, M=list<list<int>>, S=int) -> int

		Return the most equal concept in the thesaurus.
		"""
		for idx in self._concept:
			if append_concept.could_be_joined_to(self[idx], M, S): return idx
		return None

	def append_concept(self, c):
		"""
		append_concept(object, Concept) -> Id

		Add a new concept to the Thesaurus, and return the concept id.
		"""
		self._last_concept_id += 1
		self._concept[self._last_concept_id] = c
		for context in c.contexts():
			if not context in self._context: self._context[context] = self._list()
			self._context[context].append(self._last_concept_id)
		self._terms_belong_to_concept(c['='] + c['#'], self._last_concept_id)
		return self._last_concept_id

	def replace_concept_at(self, concept, idx):
		"""
		replace_concept_at(object, Concept, int) -> None

		Replaces the concept with idx id with the new concept concept.
		"""
		self._concept[idx] = concept
		self._terms_belong_to_concept(concept.et, idx)

	def delete_concept(self, cid):
		"""
		delete_concept(object, int) -> Id

		Remove a concept from the Thesaurus and its relationships.
		"""
		del self._concept[cid]
		self.remove_concept_from(cid, self._term)
		self.remove_concept_from(cid, self._context)

	def remove_concept_from(self, cid, dic):
		for (t, cs) in dic.items():
			if cid in cs:
				cs.remove(cid)
				if len(cs) == 0:
					del dic[cid]

	def _terms_belong_to_concept(self, terms, concept_idx):
		"""
		_terms_belong_to_concept(list<str>, int) -> None

		Associate terms belongs to concept concept_idx.
		"""
		for t in terms:
			if t in self._term:
				if concept_idx not in self._term[t]:
					self._term[t].append(concept_idx)
			else:
				self._term[t] = [concept_idx]

	def get_terms_of_context(self, context):
		"""
		get_terms_of_context(object, context) -> list<str>

		Return the terms of a context.
		"""
		result = []
		for concept_id in self._context[context]:
			concept = self._concept[concept_id]
			result.append(concept['='])
		return result

	def term_concepts(self, term, context=None):
		return self.concepts_from_ids(self.term_concepts_ids(term, context))

	def term_concepts_ids(self, term, context=None):
		return self.get_concepts([term], context)

	def concepts_search(self, search_expression, context=None):
		reg = self.safe_regular_expression(search_expression)
		return [ (cid, self[cid]) for cid in self.concepts() if self[cid].match(reg) ]

	def concepts_search_ids(self, search_expression, context=None):
		return [ cid for (cid, concept) in self.concepts_search(search_expression, context) ]

	def concepts_search_objects(self, search_expression, context=None):
		return [ concept for (cid, concept) in self.concepts_search(search_expression, context) ]

	def concepts_from_ids(self, cids):
		return [ self[cid] for cid in cids ]

	def correct_index(self, first_result, concepts_count):
		if first_result < 0 or concepts_count == 0:
			first_result = 0
		elif first_result > concepts_count - 1:
			first_result = concepts_count - 1
		return first_result

	def query( self, search_expression,
		narrowerthan = None, broaderthan = None, contexts = [], languages = [],
		inbranch = None, hidden = None, max_results = 5, first_result = 0 ):
		"""
		Return terms in regexp, between 'broaderthan' and 'narrowerthan' terms, in defined contexts. If inbrach is a list of terms, then returned terms are in the same branch of these. Dont return terms in except. The precedence is (TODO):
			1) Concepts whose prefered term starts with search_expression.
			2) Concepts whose prefered term has a word starting with search_expression.
			3) Concepts whose prefered term has search_expression inside.
			4) Concepts whose equivalent terms has search_expression inside.

		context == None: accept terms in all contexts.
		narrowerthan == None: no limits on top of thesaurus.
		broaderthan == None: no limits on bottom of thesaurus.
		inbranch == None: all terms.
		except == None: all terms.

		@regexp: Regular expresion.
		@narrowerthan: List of terms.
		@broaderthan: List of terms.
		@contexts: List of contexts.
		@inbranch: List of terms.
		@except: List of terms.
		@return: List of terms.

		>>> T.query('B.*', narrowerthan=['Tierra'], broaderterms=None, contexts=['geographic']
								inbranch=['America'], except=None)
		[ ... 'Bogota', 'Buenos Aires', 'Bolivia', ... ]

		>>> T.query('B.*', narrowerthan=['Escritor', 'America'],
								broaderterms=None, contexts=['geographic', 'literatura']
								inbranch=['Argentina'], except=['Borges']
		[ ... 'Cortaza', 'Sabato' ... ]

		"""
		conceptsResults = self.concepts_search(search_expression, contexts)
		conceptsResults = self.refine_search(conceptsResults, narrowerthan, broaderthan, contexts, languages, inbranch)
		conceptsResults = self.sort_by_priority(conceptsResults, search_expression, languages)

		first_result = self.correct_index(first_result, len(conceptsResults))
		return { 'concepts': [ (conceptsResults[index][1].get_prefered(languages)[0], conceptsResults[index][0]) for index in range(first_result, min(len(conceptsResults), first_result+max_results)) ],
				'concepts_count': len(conceptsResults) }
	
	def refine_search(self, conceptsResults, narrowerthan, broaderthan, contexts, languages, inbranch):
		return [ (cid, concept) for (cid, concept) in conceptsResults if self.is_in_all_concepts_transitive_relation('<', concept, narrowerthan, contexts) and self.is_in_all_concepts_transitive_relation('>', concept, broaderthan, contexts) and self.in_contexts(cid, contexts) ]
	
	def is_in_all_concepts_transitive_relation(self, relation, concept, limits, contexts):
		if limits != None:
			for term in limits:
				if not self.is_in_concepts_transitive_relation(relation, concept, term, contexts):
					return False
		return True
	
	def is_in_concepts_transitive_relation(self, relation, concept, term, contexts):
		for t in concept[relation]:
			if t == term:
				return True
			elif self.exist_term(t, contexts):
				for cid in self(t, contexts):
					if self.is_in_concepts_transitive_relation(relation, self[cid], term, contexts):
						return True
		return False

	def is_broader_than_all(self, concept, term, broaderthan):
		# TODO: REPLACE
		return True

	def sort_by_priority(self, conceptsResults, search_expression, languages):
		reg = self.safe_regular_expression(search_expression)
		startWithResults = self.concepts_prefered_terms_start_with(conceptsResults, reg, languages)
		preferedIncludesResults = self.concepts_prefered_terms_match(conceptsResults, reg, languages)
		return self.join_without_duplicates([startWithResults, preferedIncludesResults, conceptsResults])
	
	def join_without_duplicates(self, css):
		concepts_added = {}
		concepts_list = []
		for cs in css:
			for tup in cs:
				if not concepts_added.has_key(tup[0]):
					concepts_added[tup[0]] = 1
					concepts_list.append(tup)
		return concepts_list

	def concepts_prefered_terms_start_with(self, conceptsResults, reg, languages):
		return [ (cid, concept) for (cid, concept) in conceptsResults if concept.prefered_terms_start_with(reg, languages) ]

	def concepts_prefered_terms_match(self, conceptsResults, reg, languages):
		return [ (cid, concept) for (cid, concept) in conceptsResults if concept.prefered_terms_match(reg, languages) ]

	def safe_regular_expression(self, search_expression):
		import re
		try:
			reg = re.compile(search_expression, re.IGNORECASE)
			return reg
		except:
			raise KeyError, "Invalid search expression: %s\n%s" % (search_expression, sys.exc_value)

class ConceptsConflict(Exception):

	def __init__(self, value):
		self.value = value
	
	def __call__(self):
		return str(self.value)
