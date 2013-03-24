Pseudocode des Programms
========================



Hier haben wir in kurzen Stichpunkten festgehalten, was unser Programm alles können soll. Ich bitte euch vielleicht diese Liste zu ergänzen und wenn es nur irgendwie geht auch mit Programmcode zu füllen. Ob ihr nun kleine Python-Dateien schreibt und per Github verteilt und dann in diesem Dokument einen Verweis darauf hinterlegt, oder einfach den Code direkt hier rein schreibt, dass sei euch überlassen.
Viel Erfolg beim Code-Schnipsel-Suchen :‘D

P.S.: Diese Datei ist eine Markdown-Datei. Mit anderen Worten sie besitzt eine spezielle Syntax. Damit kann man sie sogar "compilieren" und bekommt alles ordentlich ausgeschrieben. Zwar haben wir nun schon in Inhaltserschließung mit Markdown zu tun gehabt, aber hier nochmal ne Reihe von Befehlen, die vielleicht hilfreich sein können. Das soll keine Schikane sein, sondern einfach nur helfen zu strukturieren. Also nehmt es mir nicht übel...


* Import XML (Subject.xml):

	* finde DESCRIPTOR (Wurzelelement)
	
		>	import xml.etree.ElementTree as ET
			tree = ET.parse('some.xml')
			root = tree.getroot() 							 #Wurzel-Element xml holen
			if root != 'concepts':
				print 'falsches Format'
				
				else:	
			
			print root									 	# Objekt an Speicherstelle
			print root.tag
			print root.attrib 							# Attribute, die zum Tag gehoeren
			print root.getchildren() 					# alle Kinderknoten auf der naechsten Ebene
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
			    rank = descriptor.find('rank').text							# zu jedem word ein rank finden
			    name = descriptor.get('name')
			    print name, rank    


	* finde alle TT,NT,UF,US,RT,BT
	* setze mit deutschen Deskriptoren gleich
	* intialisiere Deskriptoren (einzeln für jeden)
	* Packe Deskriptoren in ein Thesaurus Dict
	* Import von weiteren Formaten (JSON, CSV)
		### Import von JSON
		> import json

			with open("import.json", "r") as json_input:
				data = json.load(json_input)
			print data, type(data)

			new_data = {"Nachname": "Meier", "Vorname": "Anton"}	""hier müssen wir noch die Relationen einsetzen""	

			with open("import.json", "w") as json_output:
				json.dump(new_data, json_output)

	=> erfolgreich geladen

* Suchen:

	* genaues Wort
	* trunkiertes Wort

* Anzeigen:

	* zeige Deskiptor mit Relationen an
	* zeige einzelne Relationen an
	
			> def find_trace(deskriptorsaetze,deskriptor,trace):
			    if deskriptor:
			        trace.append(deskriptor)
			        find_trace(deskriptorsaetze, get_rel(deskriptorsaetze,deskriptor,'OB'),trace)
			    return trace
				 
	* zeige Top-Term an
	
			> def make_tree(topterm,deskriptorsaetze,level=0):
			    if level in tree_dict:
			        tree_dict[level] = tree_dict[level]+ "  " + topterm
			    else:
			        tree_dict[level] = topterm
			    if get_rel(deskriptorsaetze,topterm,'UB'):
			        for term in get_rel(deskriptorsaetze,topterm,'UB'):
			            if term:
			                make_tree(term,deskriptorsaetze,level+1)

* Bearbeiten:

	* verändere bestehenden Deskriptor/Relation
	* RT(VB) werden zu einer Liste verarbeitet und in GUI als Textbox angezeigt.
	* Speichern beendet Veränderung.
	* Löschen und Verändern wird als Bearbeiten gefasst.

* Export:
	* in XML
		### XML Export (verschiedene Methoden)
		
				xml = tostring(books)
				print '*** RAW XML ***'
				print xml
				
				print '\n*** PRETTY-PRINTED XML ***'
				dom = parseString(xml)
				print dom.toprettyxml('    ')
				
				print '*** FLAT STRUCTURE ***'
				for element in books.getiterator():
				print element.tag, '-', element.text
				
				print '\n*** TITLES ONLY ***'
				for book in books.findall('.//title'):
				print book.text

	* in JSON
		### JSON-Export
		 
				with open("new.json", "w") as json_output:
				json.dump(d, json_output)

	* in CSV
		### CSV-Export
				import csv
				with open("new_csv.csv", "w") as csv_output:
				writer = csv.writer(csv_output, delimiter=';')
					for word in d:
				writer.writerow([word, d[word]])

* GUI: