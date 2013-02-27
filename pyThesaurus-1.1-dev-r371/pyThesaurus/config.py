# begin: Platecom header
# -*- coding: latin-1 -*-
# vim: set ts=4 sts=4 sw=4 :
#
# $Id: config.py 238 2008-06-10 20:36:26Z crocha $
#
# end: Platecom header

relations            = [ '=', '-', '#', '<', '>', '!', '~' ]
relation_name        = { '=':u'Equivalentes', '-':u'Relacionados', '#':u'Ocultos', '<':u'Más ámplios', '>':u'Más específicos', '!':u'Distintos', '~':u'Similares' }

# Precedence of relations of a Concept, used for select terms of two conflictives concepts.
relations_precedence = [ '!', '<', '>', '=', '~', '-', '#' ]

# Matrix for compare two Concepts
#                            =   -   #   <   >   !   ~
matrix_comparation   = [ [  0, -3, -3, -3, -3, -5, -3 ],     # =
                          [ -3,  0, -3, -3, -3, -5, -3 ],     # -
		          [ -3, -3,  0, -3, -3, -5, -3 ],     # #
		          [ -5, -3, -3,  0, -5, -5, -3 ],     # <
		          [ -3, -3, -3, -5,  0, -5, -3 ],     # >
		          [ -5, -5, -5, -5, -5,  0, -5 ],     # !
		          [ -3, -3, -3, -3, -3, -5,  0 ], ]   # ~

# Minimum score for define similar Concepts
minimum_score = -5

