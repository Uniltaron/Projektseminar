# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: test_persistence.py 238 2008-06-10 20:36:26Z crocha $
#
# end: Platecom header

process = True

try:
	import ZODB, ZODB.FileStorage
except:
	try:
		import sys
		sys.path.append("../../parts/zope2/lib/python/")
		import ZODB, ZODB.FileStorage
		import transaction
		import persistent
	except:
		process = False

import unittest
from pyThesaurus.Thesaurus import Thesaurus
from pyThesaurus.Concept import Concept
import pyThesaurus.ioSKOSCore as SKOSCore

class testPersistence(unittest.TestCase):

	_count = 10

	def warning(self, err):
		import sys
		sys.stderr.write("\nWarning: %s. " % err)

	def error(self, err):
		import sys
		sys.stderr.write("\nERROR: %s. " % err)

	def assertEqualSets(self, a, b):
		a.sort()
		b.sort()
		self.assertEqual(a, b)

	def createDB(self):
		if not process: return
		db=ZODB.DB(ZODB.FileStorage.FileStorage('test.fs', create=1))
		self._db = db
		self._root=db.open().root()
		self._root['loadThesauri'] = False
		transaction.commit()

	def openDB(self):
		if not process: return
		db=ZODB.DB(ZODB.FileStorage.FileStorage('test.fs', create=0))
		self._db = db
		self._root=db.open().root()

	def closeDB(self):
		if not process: return
		self._db.close()
		self._db = None
		self._root = None
	
	def loadThesauri(self):
		if not process: return
		if self._root['loadThesauri']: return
		for i in range(self._count):
			skosfile = open("pyThesaurus/tests/data/sample%03i.rdf" % i)
			t = SKOSCore.load(skosfile, 'en')
			self._root['sample%03i' % i] = t
		self._root['loadThesauri'] = True
		transaction.commit()

	def delThesauri(self):
		if not process: return
		if not self._root['loadThesauri']: return
		for i in range(self._count):
			del self._root['sample%03i' % i]
		if 'ukat' in self._root['ukat']:
			del slef._root['ukat']
		self._root['loadThesauri'] = False
		transaction.commit()

	def testCreateThesaurus(self):
		if not process: return
		self.createDB()
		self.delThesauri()
		self.loadThesauri()
		t = self._root['sample000']
		self.assertEqual(t.get_prefered('animals@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('creatures@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['fr']), [])
		self.closeDB()
		
	def testOpenThesaurus(self):
		if not process: return
		self.createDB()
		self.delThesauri()
		self.loadThesauri()
		self.closeDB()
		
		self.openDB()
		self.assertEqualSets(['sample%03i' % i for i in range(self._count)] + ['loadThesauri'], self._root.keys())
		t = self._root['sample000']
		self.assertEqual(t.get_prefered('animals@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('creatures@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['fr']), [])
		t = self._root['sample001']
		self.assertEqual(t.get_prefered('wetness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('dryness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('shrubs@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('bushes@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('granite@en',  ['en']), ['rocks@en'])
		self.assertEqual(t("rocks@en"), t("basalt@en"))
		self.assertEqual(t("granite@en"), t("slate@en"))
		self.assertEqual(t("basalt@en"), t("slate@en"))
		t = self._root['sample002']
		self.assertEqual(t("abattoirs@en"), t("abattoirs@en"))
		self.assertEqual(t("abatoirs@en"), t("abattoirs@en"))
		self.assertEqual(t("abbatoirs@en"), t("abattoirs@en"))
		self.assertEqual(t("abbattoirs@en"), t("abattoirs@en"))
		self.assertEqualSets(t.get_equivalent("abbattoirs@en", ["es", "en"]), [ "abattoirs@en" ])
		t = self._root['sample003']
		self.assertEqual(t("shrubs@en"), t("shrubs@en"))
		self.assertEqual(t("bushes@en"), t("shrubs@en"))
		self.assertEqual(t("arbuste@fr"), t("shrubs@en"))
		self.assertEqual(t("buisson@fr"), t("shrubs@en"))
		self.assertEqualSets(t.get_prefered("buisson@fr", ["fr", "en"]), [ "shrubs@en", "arbuste@fr" ])
		self.assertEqualSets(t.get_prefered("buisson@fr", ["en"]), [ "shrubs@en" ])
		self.assertEqualSets(t.get_prefered("buisson@fr", ["fr"]), [ "arbuste@fr" ])

		self.closeDB()
		
	def testLoadBigThesauri(self):
		if not process: return
		self.createDB()
		self.delThesauri()
		skosfile = open("pyThesaurus/tests/data/ukat_concepts.rdf")
		t = SKOSCore.load(skosfile, 'en')
		self._root['ukat'] = t
		transaction.commit()
		self.closeDB()
		self.openDB()
		t = self._root['ukat']
		self.assertEqualSets(t.get_narrower('Educational sciences and environment@en', ['en']),  [
			u'Education and skills@en', u'Education@en', u'Educational environment@en',
			u'Educational sciences@en', u'Girls education@en', u'ICT education at school@en',
			u'Information and communication technologies education at school@en',
			u'Labor unions and education@en', u'Learning and scholarship@en', u'Learning environment@en',
			u'Learning@en', u'Libraries and education@en', u'Medieval education@en', u'Pedagogy@en',
			u'Socialism and education@en', u'Sound recordings in education@en', u'Studies@en',
			u'Study and teaching@en', u'Trade unions and education@en',
			u'Volunteer workers in education@en', u'Womens education@en'] )
		self.assertEqualSets(t.get_broader('Educational sciences and environment@en', ['en']), [])
		self.assertEqualSets(t.get_narrower('Educational policy@en', ['en']), [
			u'Adult literacy@en', u'Advancement of education@en', u'Alternative education@en',
			u'Anticurriculum movement@en', u'Business links with schools@en', 
			u'Church and college@en', u'Church and education@en', u'Community and education@en',
			u'Community links with schools@en', u'Computer uses in education@en',
			u'Computers for learning applications@en', u'Deschooling@en', u'Education and culture@en',
			u'Education and state@en', u'Educational aims@en', u'Educational alternatives@en',
			u'Educational computing@en', u'Educational development@en', u'Educational discrimination@en',
			u'Educational goals@en', u'Educational objectives@en', u'Educational policy@en',
			u'Educational strategies@en', u'Higher education and state@en', u'Industry and education@en',
			u'International cooperation education@en', u'International education@en',
			u'International understanding education@en', u'Language of instruction@en',
			u'Leisure and education@en', u'Leisure education@en', u'Right to education@en',
			u'Role of education@en', u'School industry relationship@en', u'State and education@en',
			u'Study abroad@en', u'Training abroad@en', u'Transnational education@en',
			u'Values education@en'])
		self.assertEqualSets(t.get_broader('Educational policy@en', ['en']), [])
		self.assertEqualSets(t.get_narrower('Poems@en', ['en']), [])
		self.assertEqualSets(t.get_broader('Poems@en', ['en']), [u'Basque poetry@en',
			u'Belgian poetry (French)@en', u'Breton poetry@en', u'Chinese poetry@en',
			u'English dialect poetry@en', u'English poems@en', u'English poetry@en',
			u'English prose poems@en', u'French poetry@en', u'German poetry@en', u'Greek poetry@en',
			u'Irish poetry@en', u'Italian poetry@en', u'Latin poetry@en', u'Medieval poetry@en',
			u'Middle English poetry@en', u'Persian poetry@en', u'Poetry@en', u'Russian poetry@en',
			u'Scottish poetry@en', u'Spanish poetry@en', u'Verse@en', u'Welsh poetry@en'])
		self.closeDB()
	
	def test_emanuel01_bug(self):
		if not process: return
		self.createDB()
		self.delThesauri()
		self.loadThesauri()
		self.closeDB()
		
		self.openDB()
		t = self._root['sample001']
		t.append_term(u"fútbol@es", et=[u"balón pie@es", "soccer@en", "football@en", "football@fr"])
		self._root['sample001'] = t
		transaction.commit()
		self.closeDB()

		self.openDB()
		t = self._root['sample001']
		self.assertEqualSets(t.get_equivalent(u'fútbol@es', ['es', 'en', 'fr']), [
			u"fútbol@es", u"balón pie@es", "soccer@en", "football@en", "football@fr"])
		self.closeDB()

def test_suite():
	import pdb
	suite.addTest(unittest.makeSuite(testPersistence))
	return suite


