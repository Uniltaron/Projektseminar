# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: test_skos.py 238 2008-06-10 20:36:26Z crocha $
#
# end: Platecom header

import unittest
import pyThesaurus.ioSKOSCore as SKOSCore
from pyThesaurus.Thesaurus import Thesaurus
from pyThesaurus.Concept import Concept

class testSKOSCore(unittest.TestCase):

	def warning(self, err):
		import sys
		sys.stderr.write("\nWarning: %s.\n" % err)

	def error(self, err):
		import sys
		sys.stderr.write("\nERROR: %s\n" % err)

	def assertEqualSets(self, a, b):
		a.sort()
		b.sort()
		self.assertEqual(a, b)

	def setUp(self):
		pass

	def testLoadConcept(self):
		"""
		"""
		# -----
		file = open("pyThesaurus/tests/data/sample000.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)
		self.assertEqual(t.get_prefered('animals@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('creatures@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['fr']), [])

	def testLoadLabellingProperties(self):
		"""
		|
		|
		|
		"""
		# -----
		file = open("pyThesaurus/tests/data/sample001.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)
		self.assertEqual(t.get_prefered('wetness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('dryness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('shrubs@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('bushes@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('granite@en',  ['en']), ['rocks@en'])

		self.assertEqual(t("rocks@en"), t("basalt@en"))
		self.assertEqual(t("granite@en"), t("slate@en"))
		self.assertEqual(t("basalt@en"), t("slate@en"))

		# -----
		file = open("pyThesaurus/tests/data/sample002.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqual(t("abattoirs@en"), t("abattoirs@en"))
		self.assertEqual(t("abatoirs@en"), t("abattoirs@en"))
		self.assertEqual(t("abbatoirs@en"), t("abattoirs@en"))
		self.assertEqual(t("abbattoirs@en"), t("abattoirs@en"))
		self.assertEqualSets(t.get_equivalent("abbattoirs@en", ["es", "en"]), [ "abattoirs@en" ])

		# -----
		file = open("pyThesaurus/tests/data/sample003.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqual(t("shrubs@en"), t("shrubs@en"))
		self.assertEqual(t("bushes@en"), t("shrubs@en"))
		self.assertEqual(t("arbuste@fr"), t("shrubs@en"))
		self.assertEqual(t("buisson@fr"), t("shrubs@en"))
		self.assertEqualSets(t.get_prefered("buisson@fr", ["fr", "en"]), [ "shrubs@en", "arbuste@fr" ])
		self.assertEqualSets(t.get_prefered("buisson@fr", ["en"]), [ "shrubs@en" ])
		self.assertEqualSets(t.get_prefered("buisson@fr", ["fr"]), [ "arbuste@fr" ])

		# -----
		file = open("pyThesaurus/tests/data/sample004.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)
		self.warning("prefSymbol, altSymbol are not implemented in this version")

	def testLoadDocumentationProperties(self):
		"""
		|
		|
		|
		"""
		# -----
		file = open("pyThesaurus/tests/data/sample005.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqualSets(t.get_prefered("banana republic@en", "en"), [ "banana republic@en" ])
		self.assertEqualSets(t("banana republic@en"), [ 0 ])
		self.assertEqual(t.get_publicNotes(t("banana republic@en")[0])['definition'][0], """\
A small country, especially in South and Central America, that is
		poor and often badly and immorally ruled.@en""")

		# -----
		file = open("pyThesaurus/tests/data/sample006.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqualSets(t.get_prefered("pineapples@en", "fr"), [ "ananas@fr" ])
		self.assertEqualSets(t.get_publicNotes(t("pineapples@en")[0])['definition'],
			[ unicode("The fruit of plants of the family Bromeliaceae.@en", "latin1"),
			  unicode("Le fruit de la plante herbacée de la famille des broméliacées.@fr", "latin1") ]
		)

		# -----
		file = open("pyThesaurus/tests/data/sample007.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqualSets(t.get_publicNotes(t("notebook computers@en")[0])['changenote'],
		  [{'value': u"The preferred label for this concept changed from 'laptop computers' to 'notebook computers' on 23 Jan 1999.", 'creator': {'person': {'mbox': u'mailto:jsmith@example.org', 'name': u'John Smith'}}}] )

		# -----
		file = open("pyThesaurus/tests/data/sample008.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqualSets(t.get_publicNotes(t("zoology@en")[0])['scopenote'],
		  [{'resource': u'http://www.example.com/notes/zoology.txt'}] )

		# -----
		file = open("pyThesaurus/tests/data/sample009.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqualSets(t.get_publicNotes(t("botany@en")[0])['scopenote'],
		  [{'document': {'language': {'value': u'EN', 'label': u'English'}, 'creator': {'person': {'mbox': u'mailto:jsmith@example.org', 'name': u'John Smith'}}}}] )

	def testLoadSemanticRelationships(self):
		"""
		|
		|
		|
		"""
		#
		# Broader/Narrower Relationships
		#
		file = open("pyThesaurus/tests/data/sample010.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqual(t.get_broader('mammals@en', ['en']), ['animals@en'])
		self.assertEqual(t.get_narrower('animals@en', ['en']), ['mammals@en'])

		#
		# Associative Relationships
		#
		file = open("pyThesaurus/tests/data/sample011.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqualSets(t.get_related('birds@en', ['en'], exclude=True), ['ornithology@en'])
		self.assertEqualSets(t.get_related('birds@en', ['en'], exclude=False), ['birds@en', 'ornithology@en'])
		self.assertEqualSets(t.get_related('ornithology@en', ['en'], exclude=True), ['birds@en'])

	def _testLoadMeaningfulCollectionsOfConcepts(self):
		"""
		|
		|
		|
		"""
		#
		# Labelled Collections
		#
		# Complete definition
		file = open("pyThesaurus/tests/data/sample012.rdf")
		t = SKOSCore.load(file, 'en')

		# Incomplete definition
		file = open("pyThesaurus/tests/data/sample013.rdf")
		t = SKOSCore.load(file, 'en')

		#
		# Collectable Properties
		#
		file = open("pyThesaurus/tests/data/sample014.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		#
		# Ordered Collections
		#
		# Complete definition
		file = open("pyThesaurus/tests/data/sample015.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		#
		# Ordered Collections
		#
		file = open("pyThesaurus/tests/data/sample016.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

	def _testLoadConceptSchemes(self):
		"""
		|
		|
		|
		"""
		file = open("pyThesaurus/tests/data/sample017.rdf")
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)
		self.assertEqualSet(t.schemes(), [''])

	def _testLoadSubjectIndexing(self):
		pass

	def _testLoadSubjectIndexing(self):
		pass

	def _testLoadPublishedSubjectIndicators(self):
		pass

	def _testLoadOpenIssues(self):
		pass

	def testLoadRealFile(self):
		file = open('pyThesaurus/tests/data/ukat_concepts.rdf')
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(file)

		self.assertEqualSets(t.get_narrower('Educational sciences and environment@en', ['en']),
				[u'Education and skills@en', u'Education@en', u'Educational environment@en',
					u'Educational sciences@en', u'Girls education@en', u'ICT education at school@en',
					u'Information and communication technologies education at school@en',
					u'Labor unions and education@en', u'Learning and scholarship@en',
					u'Learning environment@en', u'Learning@en', u'Libraries and education@en',
					u'Medieval education@en', u'Pedagogy@en', u'Socialism and education@en',
					u'Sound recordings in education@en', u'Studies@en', u'Study and teaching@en',
					u'Trade unions and education@en', u'Volunteer workers in education@en',
					u'Womens education@en'] )
		self.assertEqualSets(t.get_broader('Educational sciences and environment@en', ['en']), [] )
		self.assertEqualSets(t.get_narrower('Educational policy@en', ['en']),
				[ u'Adult literacy@en', u'Advancement of education@en', u'Alternative education@en',
					u'Anticurriculum movement@en', u'Business links with schools@en',
					u'Church and college@en', u'Church and education@en', u'Community and education@en',
					u'Community links with schools@en', u'Computer uses in education@en',
					u'Computers for learning applications@en', u'Deschooling@en',
					u'Education and culture@en', u'Education and state@en', u'Educational aims@en',
					u'Educational alternatives@en', u'Educational computing@en', u'Educational development@en',
					u'Educational discrimination@en', u'Educational goals@en', u'Educational objectives@en',
					u'Educational policy@en', u'Educational strategies@en', u'Higher education and state@en',
					u'Industry and education@en', u'International cooperation education@en',
					u'International education@en', u'International understanding education@en',
					u'Language of instruction@en', u'Leisure and education@en', u'Leisure education@en',
					u'Right to education@en', u'Role of education@en', u'School industry relationship@en',
					u'State and education@en', u'Study abroad@en', u'Training abroad@en',
					u'Transnational education@en', u'Values education@en'] )
		self.assertEqualSets(t.get_broader('Educational policy@en', ['en']), [])
		self.assertEqualSets(t.get_narrower('Poems@en', ['en']), [])
		self.assertEqualSets(t.get_broader('Poems@en', ['en']),
				[u'Basque poetry@en', u'Belgian poetry (French)@en', u'Breton poetry@en',
					u'Chinese poetry@en', u'English dialect poetry@en', u'English poems@en',
					u'English poetry@en', u'English prose poems@en', u'French poetry@en',
					u'German poetry@en', u'Greek poetry@en', u'Irish poetry@en', u'Italian poetry@en',
					u'Latin poetry@en', u'Medieval poetry@en', u'Middle English poetry@en',
					u'Persian poetry@en', u'Poetry@en', u'Russian poetry@en', u'Scottish poetry@en',
					u'Spanish poetry@en', u'Verse@en', u'Welsh poetry@en'])

	def _LoadSaveRealFile(self, file):
		i = open(file)
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(i)
		i.close()

		o = open('pyThesaurus/tests/data/outtest.rdf', 'w')
		io.write(o)
		o.close()

		i = open('pyThesaurus/tests/data/outtest.rdf')
		t = Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		io.read(i)
		i.close()

		return t

	def testSaveRealFile(self):
		t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample000.rdf")
		self.assertEqual(t.get_prefered('animals@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('creatures@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['fr']), [])

		t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample001.rdf")
		self.assertEqual(t.get_prefered('wetness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('dryness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('shrubs@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('bushes@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('granite@en',  ['en']), ['rocks@en'])
		self.assertEqual(t("rocks@en"), t("basalt@en"))
		self.assertEqual(t("granite@en"), t("slate@en"))
		self.assertEqual(t("basalt@en"), t("slate@en"))

		t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample002.rdf")
		self.assertEqual(t("abattoirs@en"), t("abattoirs@en"))
		self.assertEqual(t("abatoirs@en"), t("abattoirs@en"))
		self.assertEqual(t("abbatoirs@en"), t("abattoirs@en"))
		self.assertEqual(t("abbattoirs@en"), t("abattoirs@en"))
		self.assertEqualSets(t.get_equivalent("abbattoirs@en", ["es", "en"]), [ "abattoirs@en" ])

		t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample003.rdf")
		self.assertEqual(t("shrubs@en"), t("shrubs@en"))
		self.assertEqual(t("bushes@en"), t("shrubs@en"))
		self.assertEqual(t("arbuste@fr"), t("shrubs@en"))
		self.assertEqual(t("buisson@fr"), t("shrubs@en"))
		self.assertEqualSets(t.get_prefered("buisson@fr", ["fr", "en"]), [ "shrubs@en", "arbuste@fr" ])
		self.assertEqualSets(t.get_prefered("buisson@fr", ["en"]), [ "shrubs@en" ])
		self.assertEqualSets(t.get_prefered("buisson@fr", ["fr"]), [ "arbuste@fr" ])

		t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample004.rdf")
		self.warning("prefSymbol, altSymbol are not implemented in this version")

		if True: # DocumentationProperties
			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample005.rdf")
			self.assertEqualSets(t.get_prefered("banana republic@en", "en"), [ "banana republic@en" ])
			self.assertEqualSets(t("banana republic@en"), [ 0 ])
			self.assertEqual(t.get_publicNotes(t("banana republic@en")[0])['definition'][0], """A small country, especially in South and Central America, that is
		poor and often badly and immorally ruled.@en""")

			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample006.rdf")
			self.assertEqualSets(t.get_prefered("pineapples@en", "fr"), [ "ananas@fr" ])
			self.assertEqualSets(t.get_publicNotes(t("pineapples@en")[0])['definition'],
				[ unicode("The fruit of plants of the family Bromeliaceae.@en", "latin1"),
				  unicode("Le fruit de la plante herbacée de la famille des broméliacées.@fr", "latin1") ]
			)

			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample007.rdf")
			self.assertEqualSets(t.get_publicNotes(t("notebook computers@en")[0])['changenote'],
			  [{'value': u"The preferred label for this concept changed from 'laptop computers' to 'notebook computers' on 23 Jan 1999.", 'creator': {'person': {'mbox': u'mailto:jsmith@example.org', 'name': u'John Smith'}}}] )

			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample008.rdf")
			self.assertEqualSets(t.get_publicNotes(t("zoology@en")[0])['scopenote'],
			  [{'resource': u'http://www.example.com/notes/zoology.txt'}] )

			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample009.rdf")
			self.assertEqualSets(t.get_publicNotes(t("botany@en")[0])['scopenote'],
			  [{'document': {'language': {'value': u'EN', 'label': u'English'}, 'creator': {'person': {'mbox': u'mailto:jsmith@example.org', 'name': u'John Smith'}}}}] )


		if True: # Relations
			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample010.rdf")
			self.assertEqual(t.get_broader('mammals@en', ['en']), ['animals@en'])
			self.assertEqual(t.get_narrower('animals@en', ['en']), ['mammals@en'])
		
			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample011.rdf")
			self.assertEqualSets(t.get_related('birds@en', ['en'], exclude=True), ['ornithology@en'])
			self.assertEqualSets(t.get_related('birds@en', ['en'], exclude=False), ['birds@en', 'ornithology@en'])
			self.assertEqualSets(t.get_related('ornithology@en', ['en'], exclude=True), ['birds@en'])

		if False: # Collections
			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample012.rdf")
			t = SKOSCore.load(file, 'en')

			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample013.rdf")
			t = SKOSCore.load(file, 'en')

			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample014.rdf")
			t = SKOSCore.load(file, 'en')

			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample015.rdf")
			t = SKOSCore.load(file, 'en')

			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample016.rdf")
			t = SKOSCore.load(file, 'en')

		if False: # Concept Scheme
			t = self._LoadSaveRealFile("pyThesaurus/tests/data/sample017.rdf")
			t = SKOSCore.load(file, 'en')

def test_suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(testSKOSCore))
	return suite

if __name__ == '__main__':
	unittest.main()

