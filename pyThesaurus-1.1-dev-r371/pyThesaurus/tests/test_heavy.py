# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: test_heavy.py 238 2008-06-10 20:36:26Z crocha $
#
# end: Platecom header

import unittest
import pyThesaurus.ioSKOSCore as SKOSCore
from pyThesaurus.Thesaurus import Thesaurus
from pyThesaurus.Concept import Concept

class testHeavy(unittest.TestCase):

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

	def _testSearchTerm(self):
		f = open('pyThesaurus/tests/data/ukat_concepts.rdf')
		t = SKOSCore.load(f, 'en')
		self.assertEqualSets(t.search_term("physiology"), [u'Circulatory and respiratory physiology@en', u'Electrophysiology@en', u'Fatigue (physiology)@en', u'Height (physiology)@en', u'Human physiology@en', u'Musculoskeletal physiology@en', u'Neurophysiology@en', u'Plant physiology@en', u'Psychophysiology@en', u'Stress (physiology)@en', u'Weight (physiology)@en'])

	def _testContext(self):
		f = open('pyThesaurus/tests/data/ukat_concepts.rdf')
		t = SKOSCore.load(f, 'en')
		self.assertEqualSets(t.contexts(), [u'http://www.ukat.org.uk/thesaurus', u'http://www.ukat.org.uk/thesaurus/micro/105',
			u'http://www.ukat.org.uk/thesaurus/micro/110', u'http://www.ukat.org.uk/thesaurus/micro/115', u'http://www.ukat.org.uk/thesaurus/micro/120',
			u'http://www.ukat.org.uk/thesaurus/micro/125', u'http://www.ukat.org.uk/thesaurus/micro/130', u'http://www.ukat.org.uk/thesaurus/micro/135',
			u'http://www.ukat.org.uk/thesaurus/micro/140', u'http://www.ukat.org.uk/thesaurus/micro/145', u'http://www.ukat.org.uk/thesaurus/micro/150',
			u'http://www.ukat.org.uk/thesaurus/micro/155', u'http://www.ukat.org.uk/thesaurus/micro/160', u'http://www.ukat.org.uk/thesaurus/micro/165',
			u'http://www.ukat.org.uk/thesaurus/micro/170', u'http://www.ukat.org.uk/thesaurus/micro/205', u'http://www.ukat.org.uk/thesaurus/micro/210',
			u'http://www.ukat.org.uk/thesaurus/micro/215', u'http://www.ukat.org.uk/thesaurus/micro/220', u'http://www.ukat.org.uk/thesaurus/micro/225',
			u'http://www.ukat.org.uk/thesaurus/micro/230', u'http://www.ukat.org.uk/thesaurus/micro/235', u'http://www.ukat.org.uk/thesaurus/micro/240',
			u'http://www.ukat.org.uk/thesaurus/micro/245', u'http://www.ukat.org.uk/thesaurus/micro/250', u'http://www.ukat.org.uk/thesaurus/micro/255',
			u'http://www.ukat.org.uk/thesaurus/micro/260', u'http://www.ukat.org.uk/thesaurus/micro/265', u'http://www.ukat.org.uk/thesaurus/micro/270',
			u'http://www.ukat.org.uk/thesaurus/micro/275', u'http://www.ukat.org.uk/thesaurus/micro/280', u'http://www.ukat.org.uk/thesaurus/micro/285',
			u'http://www.ukat.org.uk/thesaurus/micro/305', u'http://www.ukat.org.uk/thesaurus/micro/310', u'http://www.ukat.org.uk/thesaurus/micro/315',
			u'http://www.ukat.org.uk/thesaurus/micro/320', u'http://www.ukat.org.uk/thesaurus/micro/325', u'http://www.ukat.org.uk/thesaurus/micro/330',
			u'http://www.ukat.org.uk/thesaurus/micro/335', u'http://www.ukat.org.uk/thesaurus/micro/340', u'http://www.ukat.org.uk/thesaurus/micro/345',
			u'http://www.ukat.org.uk/thesaurus/micro/350', u'http://www.ukat.org.uk/thesaurus/micro/355', u'http://www.ukat.org.uk/thesaurus/micro/360',
			u'http://www.ukat.org.uk/thesaurus/micro/365', u'http://www.ukat.org.uk/thesaurus/micro/405', u'http://www.ukat.org.uk/thesaurus/micro/410',
			u'http://www.ukat.org.uk/thesaurus/micro/415', u'http://www.ukat.org.uk/thesaurus/micro/420', u'http://www.ukat.org.uk/thesaurus/micro/425',
			u'http://www.ukat.org.uk/thesaurus/micro/430', u'http://www.ukat.org.uk/thesaurus/micro/435', u'http://www.ukat.org.uk/thesaurus/micro/440',
			u'http://www.ukat.org.uk/thesaurus/micro/445', u'http://www.ukat.org.uk/thesaurus/micro/450', u'http://www.ukat.org.uk/thesaurus/micro/505',
			u'http://www.ukat.org.uk/thesaurus/micro/510', u'http://www.ukat.org.uk/thesaurus/micro/515', u'http://www.ukat.org.uk/thesaurus/micro/520',
			u'http://www.ukat.org.uk/thesaurus/micro/525', u'http://www.ukat.org.uk/thesaurus/micro/530', u'http://www.ukat.org.uk/thesaurus/micro/535',
			u'http://www.ukat.org.uk/thesaurus/micro/540', u'http://www.ukat.org.uk/thesaurus/micro/545', u'http://www.ukat.org.uk/thesaurus/micro/605',
			u'http://www.ukat.org.uk/thesaurus/micro/610', u'http://www.ukat.org.uk/thesaurus/micro/615', u'http://www.ukat.org.uk/thesaurus/micro/620',
			u'http://www.ukat.org.uk/thesaurus/micro/625', u'http://www.ukat.org.uk/thesaurus/micro/630', u'http://www.ukat.org.uk/thesaurus/micro/635',
			u'http://www.ukat.org.uk/thesaurus/micro/640', u'http://www.ukat.org.uk/thesaurus/micro/645', u'http://www.ukat.org.uk/thesaurus/micro/650',
			u'http://www.ukat.org.uk/thesaurus/micro/655', u'http://www.ukat.org.uk/thesaurus/micro/660', u'http://www.ukat.org.uk/thesaurus/micro/665',
			u'http://www.ukat.org.uk/thesaurus/micro/670', u'http://www.ukat.org.uk/thesaurus/micro/675', u'http://www.ukat.org.uk/thesaurus/micro/680',
			u'http://www.ukat.org.uk/thesaurus/micro/685', u'http://www.ukat.org.uk/thesaurus/micro/805', u'http://www.ukat.org.uk/thesaurus/micro/810',
			u'http://www.ukat.org.uk/thesaurus/micro/815'])
		self.assertEqual(len(t.get_terms_of_context('http://www.ukat.org.uk/thesaurus/micro/110')),42)
		self.assertEqualSets(t.get_terms_of_context('http://www.ukat.org.uk/thesaurus/micro/110'), [
					[u'Access to education@en'],
					[u'Adult literacy@en'],
					[u'Alternative education@en', u'Anticurriculum movement@en', u'Deschooling@en', u'Educational alternatives@en'],
					[u'Bilingual education@en'],
					[u'Choice of school@en', u'Choosing a school@en', u'School choice and admission@en', u'School preferences@en', u'School types and choosing a school@en', u'Selection of schools@en'],
					[u'Church and education@en', u'Church and college@en'],
					[u'Community and education@en', u'Community links with schools@en'],
					[u'Compulsory education@en'],
					[u'Computer uses in education@en', u'Computers for learning applications@en', u'Educational computing@en'],
					[u'Curriculum development@en', u'Curriculum design@en', u'Curriculum improvement@en', u'Curriculum innovation@en', u'Curriculum planning@en', u'Curriculum reform@en', u'Curriculum reorganization@en'],
					[u'Democratization of education@en'],
					[u'Diversification of education@en'],
					[u'Education action zones@en'],
					[u'Education and culture@en'],
					[u'Educational development@en', u'Advancement of education@en'],
					[u'Educational discrimination@en'],
					[u'Educational experiments@en', u'Experimental education@en'],
					[u'Educational innovations@en'],
					[u'Educational objectives@en', u'Educational aims@en', u'Educational goals@en', u'Role of education@en'],
					[u'Educational opportunities@en', u'Sexual discrimination (education opportunities)@en'],
					[u'Educational policy@en'],
					[u'Educational priority areas@en'],
					[u'Educational reform@en', u'Educational change@en', u'Educational renewal@en'],
					[u'Educational strategies@en'],
					[u'Educational trends@en'],
					[u'Enrolment trends@en'],
					[u'Free education@en'],
					[u'Functional illiteracy@en'],
					[u'Illiteracy@en'],
					[u'Industry and education@en', u'Business links with schools@en', u'School industry relationship@en'],
					[u'Intercultural education@en', u'Bicultural education@en', u'Crosscultural education@en', u'Multicultural education@en'],
					[u'International education@en', u'International cooperation education@en', u'International understanding education@en', u'Values education@en'],
					[u'Language of instruction@en'],
					[u'Leisure and education@en', u'Leisure education@en'],
					[u'Mission administration@en'],
					[u'Mission policy@en'],
					[u'Right to education@en'],
					[u'School integration@en', u'Educational integration@en', u'School desegregation@en', u'School segregation@en'],
					[u'State and education@en', u'Education and state@en', u'Higher education and state@en'],
					[u'Study abroad@en', u'Training abroad@en', u'Transnational education@en'],
					[u'Teaching method innovations@en'],
					[u'Universal education@en', u'Educational equalization@en', u'Equal education@en', u'Equal opportunity (education)@en']
					])
		self.assertEqualSets(t.get_equivalent('Agriculture@en', [ 'en' ], contexts=['http://www.ukat.org.uk/thesaurus/micro/635']), 
				[u'Agricultural grants@en', u'Agriculture and state@en', u'Agriculture and the state@en', u'Agriculture, environment and natural resources@en', u'Agriculture@en', u'Arable husbandry operations@en', u'Arable husbandry@en'] )
		self.assertEqualSets(t.get_similars('Agriculture@en', [ 'en' ], contexts=['http://www.ukat.org.uk/thesaurus/micro/635']),
				[]
				)
		self.assertEqualSets(t.get_broader('Agriculture@en', [ 'en' ], contexts=['http://www.ukat.org.uk/thesaurus/micro/635']),
				[]
				)
		self.assertEqualSets(t.get_narrower('Agriculture@en', [ 'en' ], contexts=['http://www.ukat.org.uk/thesaurus/micro/635']),
				[u'Agricultural chemistry@en', u'Agricultural engineering@en', u'Agricultural practices@en', u'Agricultural research@en', u'Agriculture (farming)@en', u'Farming@en', u'Husbandry@en', u'Ranching@en']
				)
		self.assertEqualSets(t.get_related('Agriculture@en', [ 'en' ], contexts=['http://www.ukat.org.uk/thesaurus/micro/635']),
				[u'Agricultural biology@en', u'Agroclimatology@en', u'Agronomy@en', u'Animal breeding (farm)@en', u'Animal husbandry@en', u'Animal production@en', u'Cropping systems@en', u'Cultivation systems@en', u'Cultivation@en', u'Farmers@en', u'Farming systems@en', u'Forestry and community@en', u'Forestry@en', u'Forests and forestry@en', u'Livestock farming@en', u'State of cultivation@en', u'Stock farming@en']
				)

def test_suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(testHeavy))
	return suite

if __name__ == '__main__':
	unittest.main()

