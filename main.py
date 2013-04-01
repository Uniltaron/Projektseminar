#Projektseminar Wissensrepraesentation
#Konrad Kowalke, Jan Simon Scheddler, Michael Weidauer, Liesa Witt
# -*- coding: utf-8 -*-

class Deskriptorsatz(object):

	thesaurus = {} # Enthaelt alle Deskriptorsaetze

	def __init__(self,deskr): # Initialisiert einen neuen Deskriptorsatz
		try:
			if not isinstance(deskr,str): # Ueberprueft, ob es sich bei der Eingabe um einen String handelt
				print "Die Eingabe muss vom Typ String sein!"
			deskr = deskr.capitalize() # Normiert die Eingabe
			self.deskr=deskr
			self.bf=[]
			self.bs=[]
			self.ob=[]
			self.ub=[]
			self.vb=[]
			self.sb=[]
			Deskriptorsatz.thesaurus[deskr]=self # Fuegt den Deskriptorsatz ins dictionary 'thesaurus' ein
			print "Der Deskriptorsatz '%s' wurde neu angelegt!" % deskr
		except:
			print"Der Deskriptorsatz konnte nicht angelegt werden!"


	def __del__(self): # Loescht einen Deskriptorsatz, Allderdings verschwindet die Instanz erst dann ganz, wenn alle Referenzen auf diese Instanz geloescht wurden
		try:
			del Deskriptorsatz.thesaurus[deskr]
			print "Der Deskriptor wird erst vollstaendig geloescht, wenn alle weiteren Referenzen entfernt wurden!"
		except:
			print "Es ist ein Fehler beim Loeschen aufgetreten!"


	def ausgabe(self): # Gibt einen Deskriptorsatz mitsamt seiner Relationen aus
		try:
			print "%s\n________________\nBF: %s\nBS: %s\nOB: %s\nUB: %s\nVB: %s\nSB: %s\n________________\n" % (self.deskr,self.bf,self.bs,self.ob,self.ub,self.vb,self.sb)
		except:
			print "Beim Anzeigen des Deskriptorsatzes ist ein Fehler aufgetreten!"


	def add_relation(self,term,relation): # Fuegt einem Deskriptorsatz die Instanz eines eingegebenen Terms als Relationen hinzu
		try:
			term = term.capitalize() # Normiert die Eingabe
			relation = relation.upper() # Normiert die Eingabe
			if (not isinstance(term,str)) and (not isinstance(relation,str)): # Ueberprueft, ob es sich bei der Eingabe um einen String handelt
				print "Die Eingabe muss vom Typ String sein!"
			elif (term == self.deskr): # Ueberprueft, ob der Term der Deskriptor selbst ist
				print "Ein Deskriptor kann sich nicht selbst zur Relation haben!"
			elif (self.bs): # Ueberprueft, ob der Deskriptor ein Nichtdeskriptor ist
				print "Ein Nichtdeskriptor kann keine Relationen erhalten!"
			elif (term not in Deskriptorsatz.thesaurus): # Ueberprueft, ob der Term bereits als Deskriptor existiert
				print "Bitte zuerst '%s' als Deskriptorsatz anlegen!" % term
			else:
				if (relation == 'BF'):
					if (Deskriptorsatz.thesaurus[term] in self.bf): # Ueberprueft, ob der Term bereits in der Relation enthalten ist
						print "'%s' ist bereits im Deskriptorsatz enthalten!" % term
					else:
						self.bf.append(Deskriptorsatz.thesaurus[term]) # Fuegt den Term dem Deskriptorsatz hinzu
						print "Dem Deskriptorsatz wurde '%s' als neues Synonym hinzugefuegt!" % term
						Deskriptorsatz.thesaurus[term].bs.append(self) # Fuegt den Deskriptorsatz dem Term hinzu

				elif (relation == 'BS'):
					if (Deskriptorsatz.thesaurus[term] in self.bs): # Ueberprueft, ob der Term bereits in der Relation enthalten ist
						print "'%s' ist bereits im Deskriptorsatz enthalten!" % term
					elif (self.bf or self.ob or self.ub or self.vb or self.sb): # Ueberprueft, ob der Deskriptor bereits eine andere Relation hat
						print "'%s' hat bereits andere Relationen und kann daher kein Nicht-Deskriptor sein!" % term
					else:
						self.bs.append(Deskriptorsatz.thesaurus[term]) # Fuegt den Term dem Deskriptorsatz hinzu
						print "Dem Deskriptorsatz wurde '%s' als neues Symonym hinzugefuegt!\n'%s' ist jetzt ein Nicht-Deskriptor!" % term, term
						Deskriptorsatz.thesaurus[term].bf.append(self) # Fuegt den Deskriptorsatz dem Term hinzu

				elif (relation == 'OB'):
					if (self.ob): # Ueberprueft, ob der Deskriptor bereits einen Oberbegriff hat
						print "Der Deskriptor hat bereits einen Oberbegriff!"
					elif (Deskriptorsatz.thesaurus[term] in self.ob): # Ueberprueft, ob der Term bereits in der Relation enthalten ist
						print "'%s' ist bereits im Deskriptorsatz enthalten!" % term
					elif (Deskriptorsatz.thesaurus[term] in self.ub): # Ueberprueft, ob der Term bereits Unterbegriff ist
						print "'%s' ist bereits Unterbegriff des Deskriptors!" % term
					else:
						self.ob.append(Deskriptorsatz.thesaurus[term]) # Fuegt den Term dem Deskriptorsatz hinzu
						print "Dem Deskriptorsatz wurde '%s' als neuer Oberbegriff hinzugefuegt!" % term
						Deskriptorsatz.thesaurus[term].ub.append(self) # Fuegt den Deskriptorsatz dem Term hinzu

				elif (relation == 'UB'):
					if (Deskriptorsatz.thesaurus[term] in self.ub): # Ueberprueft, ob der Term bereits in der Relation enthalten ist
						print "'%s' ist bereits im Deskriptorsatz enthalten!" % term
					elif (Deskriptorsatz.thesaurus[term] in self.ob): # Ueberprueft, ob der Term bereits Oberbegriff ist
						print "'%s' ist bereits Oberbegriff des Deskriptors!" % term
					else:
						self.ub.append(Deskriptorsatz.thesaurus[term]) # Fuegt den Term dem Deskriptorsatz hinzu
						print "Dem Deskriptorsatz wurde '%s' als neuer Unterbegriff hinzugefuegt!" % term
						Deskriptorsatz.thesaurus[term].ob.append(self) # Fuegt den Deskriptorsatz dem Term hinzu

				elif (relation == 'VB'):
					if (Deskriptorsatz.thesaurus[term] in self.vb): # Ueberprueft, ob der Term bereits in der Relation enthalten ist
						print "'%s' ist bereits im Deskriptorsatz enthalten!" % term
					else:
						self.vb.append(Deskriptorsatz.thesaurus[term]) # Fuegt den Term dem Deskriptorsatz hinzu
						print "Dem Deskriptorsatz wurde '%s' als neuer verwandter Begriff hinzugefuegt!" % term
						Deskriptorsatz.thesaurus[term].vb.append(self) # Fuegt den Deskriptorsatz dem Term hinzu

				elif (relation == 'SB'):
					if (Deskriptorsatz.thesaurus[term] in self.sb): # Ueberprueft, ob der Term bereits in der Relation enthalten ist
						print "'%s' ist bereits im Deskriptorsatz enthalten!" % term
					else:
						self.sb.append(Deskriptorsatz.thesaurus[term]) # Fuegt den Term dem Deskriptorsatz hinzu
						print "Dem Deskriptorsatz wurde '%s' als neuer Spitzenbegriff hinzugefuegt!" % term

				else:
					print "Die angegebene Art von Relation existiert nicht!\nBitte benutze eine der folgenden Relationen:\nBF, BS, OB, UB, VB, SB"

		except:
			print "Beim Hinzufuegen des Terms ist ein Fehler aufgetreten!"


	def delete_relation(self,term,relation): # Entfernt die Instanz eines eingegebenen Terms aus einer beliebigen Relation
		try:
			term = term.capitalize() # Normiert die Eingabe
			relation = relation.upper() # Normiert die Eingabe
			if (not isinstance(term,str)) and (not isinstance(relation,str)): # Ueberprueft, ob es sich bei der Eingabe um einen String handelt
				print "Die Eingabe muss vom Typ String sein!"
			else:
				if (relation == 'BF'):
					if (Deskriptorsatz.thesaurus[term] not in self.bf): # Ueberprueft, ob der Term in der Relation vorhanden ist
						print "'%s' ist unter der Relation '%s' nicht zu finden!" % (term, relation)
					else:
						self.bf.remove(Deskriptorsatz.thesaurus[term]) # Entfernt den Term aus dem Deskriptor
						print "'%s' wurde erfolgreich entfernt!" % term
						Deskriptorsatz.thesaurus[term].bs.remove(self) # Entfernt den Deskriptor aus dem Term

				elif (relation == 'BS'):
					if (Deskriptorsatz.thesaurus[term] not in self.bs): # Ueberprueft, ob der Term in der Relation vorhanden ist
						print "'%s' ist unter der Relation '%s' nicht zu finden!" % (term, relation)
					else:
						self.bs.remove(Deskriptorsatz.thesaurus[term]) # Entfernt den Term aus dem Deskriptor
						print "'%s' wurde erfolgreich entfernt!" % term
						Deskriptorsatz.thesaurus[term].bf.remove(self) # Entfernt den Deskriptor aus dem Term

				elif (relation == 'OB'):
					if (Deskriptorsatz.thesaurus[term] not in self.ob): # Ueberprueft, ob der Term in der Relation vorhanden ist
						print "'%s' ist unter der Relation '%s' nicht zu finden!" % (term, relation)
					else:
						self.ob.remove(Deskriptorsatz.thesaurus[term]) # Entfernt den Term aus dem Deskriptor
						print "'%s' wurde erfolgreich entfernt!" % term
						Deskriptorsatz.thesaurus[term].ub.remove(self) # Entfernt den Deskriptor aus dem Term

				elif (relation == 'UB'):
					if (Deskriptorsatz.thesaurus[term] not in self.ub): # Ueberprueft, ob der Term in der Relation vorhanden ist
						print "'%s' ist unter der Relation '%s' nicht zu finden!" % (term, relation)
					else:
						self.ub.remove(Deskriptorsatz.thesaurus[term]) # Entfernt den Term aus dem Deskriptor
						print "'%s' wurde erfolgreich entfernt!" % term
						Deskriptorsatz.thesaurus[term].ob.remove(self) # Entfernt den Deskriptor aus dem Term

				elif (relation == 'VB'):
					if (Deskriptorsatz.thesaurus[term] not in self.vb): # Ueberprueft, ob der Term in der Relation vorhanden ist
						print "'%s' ist unter der Relation '%s' nicht zu finden!" % (term, relation)
					else:
						self.vb.remove(Deskriptorsatz.thesaurus[term]) # Entfernt den Term aus dem Deskriptor
						print "'%s' wurde erfolgreich entfernt!" % term
						Deskriptorsatz.thesaurus[term].vb.remove(self) # Entfernt den Deskriptor aus dem Term

				elif (relation == 'SB'):
					if (Deskriptorsatz.thesaurus[term] not in self.sb): # Ueberprueft, ob der Term in der Relation vorhanden ist
						print "'%s' ist unter der Relation '%s' nicht zu finden!" % (term, relation)
					else:
						self.sb.remove(Deskriptorsatz.thesaurus[term]) # Entfernt den Term aus dem Deskriptor
						print "'%s' wurde erfolgreich entfernt!" % term
		except:
			print "Beim Loeschen des Terms ist ein Fehler aufgetreten!"


def search(term): # Sucht nach einem Deskriptorsatz im Thesaurus
	try:
		if term in Deskriptorsatz.thesaurus: # Ueberprueft, ob der Suchbegriff im Thesaurus enthalten ist
			Deskriptorsatz.thesaurus[term].ausgabe() # Wenn ja, gibt er diesen aus
		else:
			print "Begriff konnte nicht gefunden werden!"
	except:
		print "Waehrend der Suche ist ein Fehler aufgetreten!"



##############Test##############

Deskriptorsatz('Hund')
Deskriptorsatz('Pudel')
Deskriptorsatz.thesaurus['Hund'].add_relation('Pudel','ub')


##############TUI##############

counter = 1
while counter == 1:
	print "Waehle eine der folgenden Optionen aus:"
	print "1. Importiere einen Thesaurus!"
	print "2. Exportiere einen Thesaurus!"
	print "3. Lege einen neuen Deskriptorsatz an!"
	print "4. Loesche einen Deskriptorsatz!"
	print "5. Fuege einem Deskriptorsatz einen neuen Term hinzu!"
	print "6. Loesche einen Term aus einem Deskriptorsatz!"
	print "7. Suche einen Deskriptorsatz!"
	print "8. Zeige einen Deskriptorsatz an!"
	print "9. Beenden"

	eingabe = raw_input()
	try:
		eingabe = int(eingabe)
	except ValueError:
		print "Bitte eine Zahl eingeben..."
		eingabe = 1

	if eingabe == 1:
		print "Funktion existiert noch nicht!"
	elif eingabe == 2:
		print "Funktion existiert noch nicht!"
	elif eingabe == 3:
		input = raw_input("Gib den Titel des neuen Deskriptors an!")
		Deskriptorsatz(input)
	elif eingabe == 4:
		input = raw_input("Gib den Titel des zu loeschenden Deskriptors an!")
		input = input.capitalize()
		del Deskriptorsatz.thesaurus[input]
	elif eingabe == 5:
		input_a = raw_input("Gib den Titel des Deskriptorsatzes an, dem der neue Term hinzugefuegt werden soll\n")
		input_a = input_a.capitalize()
		input_b = raw_input("Gib den Term an, der hinzugefuegt werden soll\n")
		input_b = input_b.capitalize()
		input_c = raw_input("Gib die Relation an, welcher du den Term hinzufuegen moechtest!\n")
		input_c = input_c.upper()
		Deskriptorsatz.thesaurus[input_a].add_relation(input_b,input_c)
	elif eingabe == 6:
		input_a = raw_input("Gib den Titel des Deskriptorsatzes an, aus welchem der Term entfernt werden soll\n")
		input_a = input_a.capitalize()
		input_b = raw_input("Gib den Term an, der entfernt werden soll\n")
		input_b = input_b.capitalize()
		input_c = raw_input("Gib die Relation an, aus welcher der Term entfernt werden soll\n")
		input_c = input_c.upper()
		Deskriptorsatz.thesaurus[input_a].delete_relation(input_b,input_c)
	elif eingabe == 7:
		input = raw_input("Gib einen Suchbegriff ein!\n")
		input = input.capitalize()
		search(input)
	elif eingabe == 8:
		input = raw_input("Gib den Titel des Deskriptorsatzes ein, den du anzeigen moechtest\n")
		input = input.capitalize()
		Deskriptorsatz.thesaurus[input].ausgabe()
	elif eingabe == 9:
		counter = 2
	else:
		print "Bitte gib eine Zahl zwischen 1 und 9 ein!"