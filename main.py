#Projektseminar WissensreprÃ¤sentation
#Konrad Kowalke, Jan Simon Scheddler, Michael Weidauer, Liesa Witt
# -*- coding: utf-8 -*-

# Thesaurus befindet sich innerhalb der Klasse Deskriptorsatz
# Deskriptorsätze werden anhand dessen key im dictionary 'Deskriptorsatz.thesaurus' aufgerufen

class Deskriptorsatz(object):
    thesaurus = {}
# Legt einen neuen Deskriptorsatz an, dieser enthÃ¤lt noch keine Relationen
# ÃœberprÃ¼ft zuerst, ob es sich beim Namen des Deskriptorsatzes um einen String handelt 
# Die Instanz wird dem dictionary 'thesaurus' unter dessen Name hinzugefügt
# Bsp.: Deskriptorsatz('Hund')      legt einen neuen Deskriptorsatz Hund an und speichert diesen im dictionary Deskriptorsatz.thesaurus 

    def __init__(self,deskr):
        try:
            if not isinstance(deskr,str):
                raise Exception()
            deskr = deskr.capitalize()
            self.deskr=deskr
            self.bf=[]
            self.bs=[]
            self.ob=[]
            self.ub=[]
            self.vb=[]
            self.sb=[]
            Deskriptorsatz.thesaurus[deskr]=self
            print "Der Deskriptorsatz '%s' wurde neu angelegt!\n" % deskr
        except:
            print"Der Deskriptorsatz konnte nicht angelegt werden!\n"

# Löscht einen Deskriptorsatz
# Allderdings verschwindet die Instanz erst dann ganz, wenn alle Referenzen auf diese Instanz gelöscht wurden
    def __del__(self):
        try:
            del Deskriptorsatz.thesaurus[deskr]
        except:
            print "Es ist ein Fehler beim LÃ¶schen aufgetreten!\nEntfernen Sie erst alle anderen Referenzen!"
    
# Gibt einen Deskriptorsatz mitsamt seiner Relationen aus

    def ausgabe(self):
        try:
            print "%s\n________________\nBF: %s\nBS: %s\nOB: %s\nUB: %s\nVB: %s\nSB: %s\n________________\n" % (self.deskr,self.bf,self.bs,self.ob,self.ub,self.vb,self.sb)
        except:
            print "Beim Anzeigen des Deskriptorsatzes ist ein Fehler aufgetreten!\n"



# Fügt einem Deskriptorsatz die Instanz eines eingegebenen Terms als Relationen hinzu
# Erfordert, dass der Term bereits als Deskriptorsatz angelegt wurde
# Überprüft zuerst, ob es sich bei der Eingabe um einen String handelt
# Fügt im Umkehrschluss der Instanz des eingegebenen Terms die Instanz des Diskriptorsatzes hinzu 

    def add_relation(self,term,relation):
        try:
            term = term.capitalize()
            relation = relation.upper()
            if (not isinstance(term,str)) and (not isinstance(relation,str)):
                raise Exception()
            elif (term == self.deskr):
                print "Ein Deskriptor kann sich nicht selbst zur Relation haben!\n"
            elif (self.bs):
                print "Ein Nichtdeskriptor kann keine Relationen erhalten!\n"
            elif (term not in Deskriptorsatz.thesaurus):
                print "Bitte zuerst '%s' als Deskriptorsatz anlegen!\n" % term
            else:
                if (relation == 'BF'):
                    if (Deskriptorsatz.thesaurus[term] in self.bf):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    else:
                        self.bf.append(Deskriptorsatz.thesaurus[term])
                        print "Dem Deskriptorsatz wurde '%s' als neues Synonym hinzugefÃ¼gt!\n" % term
                        Deskriptorsatz.thesaurus[term].bs.append(self)

                elif (relation == 'BS'):
                    if (Deskriptorsatz.thesaurus[term] in self.bs):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    elif (self.bf or self.ob or self.ub or self.vb or self.sb):
                        print "'%s' hat bereits andere Relationen und kann daher kein Nicht-Deskriptor sein!\n" % term
                    else:
                        self.bs.append(Deskriptorsatz.thesaurus[term])
                        print "Dem Deskriptorsatz wurde '%s' als neues Symonym hinzugefÃ¼gt!\n'%s' ist jetzt ein Nicht-Deskriptor!\n" % term, term
                        
                elif (relation == 'OB'):
                    if (self.ob):
                        print "Der Deskriptor hat bereits einen Oberbegriff!\n"
                    elif (Deskriptorsatz.thesaurus[term] in self.ob):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    elif (Deskriptorsatz.thesaurus[term] in self.ub):
                        print "'%s' ist bereits Unterbegriff des Deskriptors!\n" % term
                    else:
                        self.ob.append(Deskriptorsatz.thesaurus[term])
                        print "Dem Deskriptorsatz wurde '%s' als neuer Oberbegriff hinzugefÃ¼gt!\n" % term
                        Deskriptorsatz.thesaurus[term].ub.append(self)

                elif (relation == 'UB'):
                    if (Deskriptorsatz.thesaurus[term] in self.ub):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    elif (Deskriptorsatz.thesaurus[term] in self.ob):
                        print "'%s' ist bereits Oberbegriff des Deskriptors!" % term
                    else:
                        self.ub.append(Deskriptorsatz.thesaurus[term])
                        print "Dem Deskriptorsatz wurde '%s' als neuer Unterbegriff hinzugefÃ¼gt!\n" % term
                        Deskriptorsatz.thesaurus[term].ob.append(self)

                elif (relation == 'VB'):
                    if (Deskriptorsatz.thesaurus[term] in self.vb):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    else:
                        self.vb.append(Deskriptorsatz.thesaurus[term])
                        print "Dem Deskriptorsatz wurde '%s' als neuer verwandter Begriff hinzugefÃ¼gt!\n" % term
                        Deskriptorsatz.thesaurus[term].vb.append(self)

                elif (relation == 'SB'):
                    if (Deskriptorsatz.thesaurus[term] in self.sb):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    else:
                        self.sb.append(Deskriptorsatz.thesaurus[term])
                        print "Dem Deskriptorsatz wurde '%s' als neuer Spitzenbegriff hinzugefÃ¼gt!\n" % term

                else:
                    print "Die angegebene Art von Relation existiert nicht!\nBitte benutze eine der folgenden Relationen:\nBF, BS, OB, UB, VB, SB\n"
        except:
            print "Beim HinzufÃ¼gen des Terms ist ein Fehler aufgetreten!"



# Entfernt einen die Instanz eines eingegebenen Terms aus einer beliebigen Relation
# ÃœberprÃ¼ft zuerst, ob es sich bei der Eingabe um einen String handelt
# Entfernt im Umkehrschluss die Instanz des Deskriptorsatzes aus der Instanz des Terms

    def delete_relation(self,term,relation):
        try:
            term = term.capitalize()
            relation = relation.upper() 
            if (not isinstance(term,str)) and (not isinstance(relation,str)):
                raise Exception()
            else:
                if (relation == 'BF'):
                    if (Deskriptorsatz.thesaurus[term] not in self.bf):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.bf.remove(Deskriptorsatz.thesaurus[term])
                        print "'%s' wurde erfolgreich entfernt!\n" % term
                        Deskriptorsatz.thesaurus[term].bs.remove(self)

                elif (relation == 'BS'):
                    if (Deskriptorsatz.thesaurus[term] not in self.bs):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.bs.remove(Deskriptorsatz.thesaurus[term])
                        print "'%s' wurde erfolgreich entfernt!\n" % term
                        Deskriptorsatz.thesaurus[term].bf.remove(self)

                elif (relation == 'OB'):
                    if (Deskriptorsatz.thesaurus[term] not in self.ob):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.ob.remove(Deskriptorsatz.thesaurus[term])
                        print "'%s' wurde erfolgreich entfernt!\n" % term
                        Deskriptorsatz.thesaurus[term].ub.remove(self)

                elif (relation == 'UB'):
                    if (Deskriptorsatz.thesaurus[term] not in self.ub):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.ub.remove(Deskriptorsatz.thesaurus[term])
                        print "'%s' wurde erfolgreich entfernt!\n" % term
                        Deskriptorsatz.thesaurus[term].ob.remove(self)

                elif (relation == 'VB'):
                    if (Deskriptorsatz.thesaurus[term] not in self.vb):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.vb.remove(Deskriptorsatz.thesaurus[term])
                        print "'%s' wurde erfolgreich entfernt!\n" % term
                        Deskriptorsatz.thesaurus[term].vb.remove(self)

                elif (relation == 'SB'):
                    if (Deskriptorsatz.thesaurus[term] not in self.sb):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.sb.remove(Deskriptorsatz.thesaurus[term])
                        print "'%s' wurde erfolgreich entfernt!\n" % term
        except:
            print "Beim Löschen des Terms ist ein Fehler aufgetreten!\n"


    def suche(term):
        pass

#****************Test****************#

'''if __name__ == '__main__':
    Hund = Deskriptorsatz('hund')
    Katze = Deskriptorsatz('Katze')
    Tier = Deskriptorsatz('Tier')
    Pudel = Deskriptorsatz('Pudel')
    Hund.add_relation('Saeuegetier','OB')
    Hund.add_relation('pudel','UB')
    Hund.add_relation('DACKEL','UB')
    Hund.add_relation('Hundefutter','VB')
    Hund.add_relation('Raubtier','OB')
'''

Deskriptorsatz('Hund')
Deskriptorsatz('Pudel')
Deskriptorsatz.thesaurus['Hund'].add_relation('Pudel','ub')



