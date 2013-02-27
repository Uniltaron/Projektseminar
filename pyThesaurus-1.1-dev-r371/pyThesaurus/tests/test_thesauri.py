# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: test_thesauri.py 361 2008-07-31 22:07:50Z flarumbe $
#
# end: Platecom header

import unittest
from pyThesaurus.Thesaurus import Thesaurus
from pyThesaurus.Concept import Concept
import pyThesaurus.ioSKOSCore as SKOSCore

class testThesauri(unittest.TestCase):

    def assertEqualSets(self, a, b):
        a.sort()
        b.sort()
        self.assertEqual(a, b)

    def setUp(self):
        self.thesaurus = Thesaurus()

    def testConceptEquivalent(self):
        """
        """
        c = Concept(et = ["shrubs@en", "bushes@en", "arbuste@fr", "buisson@fr"])
        self.thesaurus.append_concept(c)

        # Share same concept
        self.assertEqual(self.thesaurus("shrubs@en"), self.thesaurus("bushes@en"))
        self.assertEqual(self.thesaurus("bushes@en"), self.thesaurus("arbuste@fr") )
        self.assertEqual(self.thesaurus("arbuste@fr"), self.thesaurus("buisson@fr") )

        # Prefered labels
        self.assertEqual(self.thesaurus.get_prefered("shrubs@en",  ["en"]), ["shrubs@en"])
        self.assertEqual(self.thesaurus.get_prefered("bushes@en",  ["en"]), ["shrubs@en"])
        self.assertEqual(self.thesaurus.get_prefered("arbuste@fr", ["fr"]), ["arbuste@fr"])
        self.assertEqual(self.thesaurus.get_prefered("buisson@fr", ["fr"]), ["arbuste@fr"])

        self.thesaurus.set_prefered("bushes@en", self.thesaurus("bushes@en")[0])

        self.assertEqual(self.thesaurus.get_prefered("shrubs@en", ["en"]), ["bushes@en"])
        self.assertEqual(self.thesaurus.get_prefered("bushes@en", ["en"]), ["bushes@en"])
        self.assertEqual(self.thesaurus.get_prefered("arbuste@fr", ["fr"]), ["arbuste@fr"])
        self.assertEqual(self.thesaurus.get_prefered("buisson@fr", ["fr"]), ["arbuste@fr"])

        self.thesaurus.set_prefered("buisson@fr", self.thesaurus("bushes@en")[0])

        self.assertEqual(self.thesaurus.get_prefered("shrubs@en", ["en"]), ["bushes@en"])
        self.assertEqual(self.thesaurus.get_prefered("bushes@en", ["en"]), ["bushes@en"])
        self.assertEqual(self.thesaurus.get_prefered("arbuste@fr", ["fr"]), ["buisson@fr"])
        self.assertEqual(self.thesaurus.get_prefered("buisson@fr", ["fr"]), ["buisson@fr"])

        #
        self.assertEqualSets(
                self.thesaurus.get_equivalent("shrubs@en", ["en","fr"]),
                ["shrubs@en", "bushes@en", "arbuste@fr", "buisson@fr"])

        #
        self.assertEqualSets(
                self.thesaurus.get_equivalent("shrubs@en", ["en"]),
                ["shrubs@en", "bushes@en"])

        #
        self.assertEqualSets(
                self.thesaurus.get_equivalent("shrubs@en", ["fr"]),
                ["arbuste@fr", "buisson@fr"])

        #
        self.assertEqualSets(
                self.thesaurus.get_equivalent("shrubs@en", ["es"]),
                [])

    def testTerm(self):
        """
        """
        self.thesaurus.append_term('economic cooperation@en',
                et=['economic co-operation@en'],
                rt=['interdependence@en'],
                bt=['economic policy@en'],
                ht=['economic coperation@en'],
                nt=['european economic cooperation@en',
                    'european industrial cooperation@en',
                    'industrial cooperation@en'])

        # Test equal concepts
        self.assertEqual(self.thesaurus('economic cooperation@en'), self.thesaurus('economic co-operation@en'))

        # Test borrow and narrow
        self.assertEqual(self.thesaurus.get_prefered('economic co-operation@en', ["en"]), ['economic cooperation@en'])
        self.assertEqual(self.thesaurus.get_prefered('economic co-operation@en', ["es"]), [])
        self.assertEqual(self.thesaurus.get_broader('economic cooperation@en', ['en']), ['economic policy@en'])
        self.assertEqualSets(self.thesaurus.get_narrower('economic cooperation@en', ['en']),
                ['european economic cooperation@en', 'european industrial cooperation@en', 'industrial cooperation@en'])
        self.assertEqual(self.thesaurus.get_related('economic cooperation@en', ['en']), ['interdependence@en'])

        # Test Hidden terms
        self.assertEqualSets(self.thesaurus.get_equivalent("economic coperation@en", ["en","fr"]),
                ['economic cooperation@en', 'economic co-operation@en'])
        self.assertEqual(self.thesaurus.get_prefered('economic coperation@en', ["en"]), ['economic cooperation@en'])

    def testSearchTerm(self):
        """
        """
        self.thesaurus.append_term('economic cooperation@en',
                et=['economic co-operation@en'],
                rt=['interdependence@en'],
                bt=['economic policy@en'],
                ht=['economic coperation@en'],
                nt=['european economic cooperation@en',
                    'european industrial cooperation@en',
                    'industrial cooperation@en'])
        self.assertEqualSets(self.thesaurus.search_term("coop"), ['economic cooperation@en'])

        # Test equal concepts

    def testThesaurusQuery(self):
        """
        """
        skosfile = open("../pyThesaurus/pyThesaurus/tests/data/hierarchy.rdf")
        t = SKOSCore.load(skosfile, 'es')

        results = t.query("xno", narrowerthan = ['xnodo1@es'], languages = ['es'])
        self.results_have_terms(results, ['xnodo2@es','xnodo3@es','xnodo4@es','xnodo9@es'], ['es'])

        results = t.query("xno", narrowerthan = ['xnodo6@es'], languages = ['es'])
        self.results_have_terms(results, ['xnodo5@es','xnodo7@es','xnodo8@es','xnodo4@es','xnodo9@es'], ['es'])

        results = t.query("xno", narrowerthan = ['xnodo8@es'], languages = ['es'])
        self.results_have_terms(results, ['xnodo4@es','xnodo9@es'], ['es'])
        
        results = t.query("xno", narrowerthan = ['xnodo7@es'], languages = ['es'])
        self.results_have_terms(results, ['xnodo4@es'], ['es'])
        
        results = t.query("xno", broaderthan = ['xnodo7@es'], languages = ['es'])
        self.results_have_terms(results, ['xnodo6@es'], ['es'])
        
        results = t.query("xno", broaderthan = ['xnodo4@es'], languages = ['es'])
        self.results_have_terms(results, ['xnodo7@es','xnodo8@es','xnodo6@es','xnodo3@es','xnodo1@es'], ['es'])

    def results_have_terms(self, results, terms, languages):
        self.assertEqualSets([term for (term, cid) in results['concepts']], terms)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testThesauri))
    return suite

if __name__ == '__main__':
    suiteFew = unittest.TestSuite()
    suiteFew.addTest(testThesauri("testConceptEquivalent"))
    unittest.TextTestRunner(verbosity=2).run(test_suite())

