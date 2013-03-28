import csv, sys, json
import xml.etree.ElementTree as ET



def import_csv(filename):
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
    
    
def export_json(filename):
	with open(filename, "r") as json_input:
    data = json.load(json_input)
		print data, type(data)
		
	new_data={}

	with open("new_some.json", "w") as json_output:
    json.dump(new_data, json_output)		
		
		
			
def import_xml(filename):
	tree = ET.parse(filename)					
	root = tree.getroot()						 #Wurzel-Element xml holen
	if root != 'concepts':
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

	for descriptor in root.findall('descriptor'):					#jedes "word finden"
		rank = descriptor.find('rank').text						# zu jedem word ein rank finden
		name = descriptor.get('name')
		print name, rank    
    

