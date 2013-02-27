# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: test_io.py 238 2008-06-10 20:36:26Z crocha $
#
# end: Platecom header

import unittest
import pyThesaurus.ioSKOSCore as SKOSCore
import pyThesaurus.ioDing as Ding
from pyThesaurus.Thesaurus import Thesaurus
from pyThesaurus.Concept import Concept

class testIO(unittest.TestCase):

	def warning(self, err):
		import sys
		sys.stderr.write("\nWarning: %s. " % err)

	def error(self, err):
		import sys
		sys.stderr.write("\nERROR: %s\n" % err)

	def assertEqualSets(self, a, b):
		a.sort()
		b.sort()
		self.assertEqual(a, b)

	def setUp(self):
		pass

	def testSkos(self):
		t=Thesaurus()
		io = SKOSCore.ioSKOSCore("en", thesaurus=t, contexts=[])
		file = open("pyThesaurus/tests/data/sample000.rdf")
		io.read(file)
		file = open("pyThesaurus/tests/data/sample001.rdf")
		io.read(file)
		self.assertEqual(t.get_prefered('animals@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('creatures@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['fr']), [])
		self.assertEqual(t.get_prefered('wetness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('dryness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('shrubs@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('bushes@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('granite@en',  ['en']), ['rocks@en'])
		self.assertEqual(t("rocks@en"), t("basalt@en"))
		self.assertEqual(t("granite@en"), t("slate@en"))
		self.assertEqual(t("basalt@en"), t("slate@en"))

	def testDing(self):
		t = Thesaurus()
		io = Ding.ioDing("en",thesaurus=t, contexts=[])
		file = open("pyThesaurus/tests/data/sample000.txt")
		io.read(file)
		file = open("pyThesaurus/tests/data/sample001.txt")
		io.read(file)
		self.assertEqual(t.get_prefered('animals@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('creatures@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['en']), ['animals@en'])
		self.assertEqual(t.get_prefered('fauna@en',  ['fr']), [])
		self.assertEqual(t.get_prefered('wetness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('dryness@en',  ['en']), ['wetness@en'])
		self.assertEqual(t.get_prefered('shrubs@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('bushes@en',  ['en']), ['shrubs@en'])
		self.assertEqual(t.get_prefered('granite@en',  ['en']), ['rocks@en'])
		self.assertEqual(t("rocks@en"), t("basalt@en"))
		self.assertEqual(t("granite@en"), t("slate@en"))
		self.assertEqual(t("basalt@en"), t("slate@en"))

	def testDing2(self):
		t = Thesaurus()
		io = Ding.ioDing("es",thesaurus=t, contexts=[])
		file = open("pyThesaurus/tests/data/open_thesaurus_es.txt")
		io.read(file, encoding='latin1')
		self.assertEqual(t.get_prefered('rector@es',  ['es']), [u'abad@es', unicode('de\xe1n@es','latin1')])

	def testDing3(self):
		t = Thesaurus()
		c = Concept(et = ["shrubs@en", "bushes@en", "arbuste@fr", "buisson@fr"])
		t.append_concept(c)
		io = Ding.ioDing("en",thesaurus=t, contexts=[])
		file = open("test.txt", "w")
		io.write(file, encoding='latin1')
		file.close()

		file = open("test.txt")
		self.assertEqual(file.readlines()[0][0:-2], "shrubs;bushes")
		file.close()

	def testDing4(self):
		t = Thesaurus()
		io = Ding.ioDing("es",thesaurus=t, contexts=[])
		file = open("pyThesaurus/tests/data/sample002.txt")
		io.read(file)
		self.assertEqual(t.terms(), [u'bushes@es', u'rocks@es', u'basalt@es', u'wetness@es', u'shrubs@es', u'dryness @es', u'granite@es', u'slate@es'])

def test_suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(testIO))
	return suite

if __name__ == '__main__':
	unittest.main()
