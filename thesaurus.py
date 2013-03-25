#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Gruppe 412
# Liesa Witt, Jan Simon Scheddler, Konrad Kowalke, Michael Weidauer
# Deskriptorsatz Relationen werden festgelegt

thesaurus={}

class Deskriptorsatz(object):
    def __init__(self, deskriptor, BF=[], BS=[], OB=[], UB=[] ,VB=[], SB=[] ): # ENGL BEDEUTUNGEN !!!!
        try:
             if not isinstance(deskriptor,basestring):
                 raise Exception()
            self.deskriptor = deskriptor
            self.BF = BF
            self.BS = BS
            self.OB = OB
            self.UB = UB
            self.VB = VB
            self.SB = SB
            thesaurus[deskriptor]=self
        except:
            print"Ja, scheiße! Klappt nich XD"
"""
# import einer csv datei

import csv, sys
	filename='anyfile.csv'
	with open ('filname.csv', 'r') as data: 
		reader = csv.reader(data, delimiter=';')
		 try:
        	for row in reader:
            	print row
   		 except csv.Error as error:
        	sys.exit('file %s, line %d: %s' % (filename, reader.line_num, error))

			
	with open('new_some.csv', 'w') as new_data:
    writer = csv.writer(new_data, delimiter=';')
    writer.writerows(list_data)
    
    
    
# import einer json datei
import json
	with open("some.json", "r") as json_input:
    data = json.load(json_input)
		print data, type(data)
		
new_data={}

	with open("new_some.json", "w") as json_output:
    json.dump(new_data, json_output)		
		
		
# auslesen einer xml datei und finden des wurzelelements
			
import xml.etree.ElementTree as ET
tree = ET.parse('subject.xml')						
root = tree.getroot() 							 #Wurzel-Element xml holen
if root != 'CONCEPT':
	print 'falsches Format'

else:	

print root										 # Objekt an Speicherstelle
print root.tag
print root.attrib 								 # Attribute, die zum Tag gehoeren
print root.getchildren() 						# alle Kinderknoten auf der naechsten Ebene
												# Pruefen, ob es weitere Kinderknoten gibt:


if root.getchildren():
    print "Es gibt weitere Kinderknoten"
else:
    print "Keine weitere Kinderknoten vorhanden"
for child in root:
    print child.tag, child.attrib, child.text
    
words = root.getchildren()

for descriptor in descriptoren:
    discriptor.tag, discriptor, attrib

for descriptor in root.findall('DESCRIPTOR'):					#jedes "word finden"
    rank = descriptor.find('rank').text						# zu jedem word ein rank finden
    name = descriptor.get('name')
    print name, rank    
"""    

