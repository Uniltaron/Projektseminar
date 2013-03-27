#Projektseminar Wissensrepräsentation
#Konrad Kowalke, Jan Simon Scheddler, Liesa Witt, Michael Weidauer
# -*- coding: utf-8 -*-

thesaurus = {}

class deskriptorsatz(object):


# Legt einen neuen Deskriptorsatz an, dieser enthält noch keine Relationen
# Überprüft zuerst, ob es sich bei der Eingabe um einen String handelt 
# Erlaubt jedoch auch Eingaben wie '23'

    def __init__(self,deskr):
        try:
            if not isinstance(deskr,str):
                raise Exception()
            #deskr = deskr.capitalize()
            self.deskr=deskr
            self.bf=[]
            self.bs=[]
            self.ob=[]
            self.ub=[]
            self.vb=[]
            self.sb=[]
            thesaurus[deskr]=self
        except:
            print"Der Deskriptorsatz konnte nicht angelegt werden!\n"


    def __del__(self):
        try:
            del thesaurus[deskr]
        except:
            print "Es ist ein Fehler beim Löschen aufgetreten!"


    def delete_deskriptorsatz(self):
        self = None
    
# Gibt einen Deskriptorsatz mitsamt seiner Relationen aus

    def ausgabe(self):
        try:
            print "%s\n________________\nBF: %s\nBS: %s\nOB: %s\nUB: %s\nVB: %s\nSB: %s\n________________\n" % (self.deskr,self.bf,self.bs,self.ob,self.ub,self.vb,self.sb)
        except:
            print "Beim Anzeigen des Deskriptorsatzes ist ein Fehler aufgetreten!\n"



# Fügt einem Deskriptorsatz einen neuen Term zu einer beliebigen Relation hinzu
# Überprüft zuerst, ob es sich bei der Eingabe um einen String handelt

    def add_relation(self,term,relation):
        try:
            term = term.capitalize()
            relation = relation.upper()
            if (not isinstance(term,str)) and (not isinstance(relation,str)):
                raise Exception()
            elif (term is self.deskr):
                print "Ein Deskriptor kann sich nicht selbst zur Relation haben!\n"
            elif (self.bs):
                print "Ein Nichtdeskriptor kann keine Relationen erhalten!\n"
            else:
                if (relation is 'BF'):
                    if (term in self.bf):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    else:
                        self.bf.append(term)
                        print "Dem Deskriptorsatz wurde '%s' als neues Synonym hinzugefügt!\n" % term

                elif (relation is 'BS'):
                    if (term in self.bs):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    elif (self.bf or self.ob or self.ub or self.vb or self.sb):
                        print "'%s' hat bereits andere Relationen und kann daher kein Nicht-Deskriptor sein!\n" % term
                    else:
                        self.bs.append(term)
                        print "Dem Deskriptorsatz wurde '%s' als neues Symonym hinzugefügt!\n'%s' ist jetzt ein Nicht-Deskriptor!\n" % term, term
                        
                elif (relation is 'OB'):
                    if (self.ob):
                        print "Der Deskriptor hat bereits einen Oberbegriff!\n"
                    elif (term in self.ob):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    elif (term in self.ub):
                        print "'%s' ist bereits Unterbegriff des Deskriptors!\n" % term
                    else:
                        self.ob.append(term)
                        print "Dem Deskriptorsatz wurde '%s' als neuer Oberbegriff hinzugefügt!\n" % term

                elif (relation is 'UB'):
                    if (term in self.ub):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    elif (term in self.ob):
                        print "'%s' ist bereits Oberbegriff des Deskriptors!" % term
                    else:
                        self.ub.append(term)
                        print "Dem Deskriptorsatz wurde '%s' als neuer Unterbegriff hinzugefügt!\n" % term

                elif (relation is 'VB'):
                    if (term in self.vb):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    else:
                        self.vb.append(term)
                        print "Dem Deskriptorsatz wurde '%s' als neuer verwandter Begriff hinzugefügt!\n" % term

                elif (relation is 'SB'):
                    if (term in self.sb):
                        print "'%s' ist bereits im Deskriptorsatz enthalten!\n" % term
                    else:
                        self.sb.append(term)
                        print "Dem Deskriptorsatz wurde '%s' als neuer Spitzenbegriff hinzugefügt!\n" % term

                else:
                    print "Die angegebene Art von Relation existiert nicht!\nBitte benutze eine der folgenden Relationen:\nBF, BS, OB, UB, VB, SB\n"
        except:
            print "Beim Hinzufügen des Terms ist ein Fehler aufgetreten!"



# Entfernt einen Term aus einer beliebigen Relation
# Überprüft zuerst, ob es sich bei der Eingabe um einen String handelt

    def delete_relation(self,term,relation):
        try:
            term = term.capitalize()
            relation = relation.upper() 
            if (not isinstance(term,str)) and (not isinstance(relation,str)):
                raise Exception()
            else:
                if (relation is 'BF'):
                    if (term not in self.bf):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.bf.remove(term)
                        print "'%s' wurde erfolgreich entfernt!\n" % term

                elif (relation is 'BS'):
                    if (term not in self.bs):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.bs.remove(term)

                elif (relation is 'OB'):
                    if (term not in self.ob):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.ob.remove(term)
                        print "'%s' wurde erfolgreich entfernt!\n" % term

                elif (relation is 'UB'):
                    if (term not in self.ub):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.ub.remove(term)
                        print "'%s' wurde erfolgreich entfernt!\n" % term

                elif (relation is 'VB'):
                    if (term not in self.vb):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.vb.remove(term)
                        print "'%s' wurde erfolgreich entfernt!\n" % term

                elif (relation is 'SB'):
                    if (term not in self.sb):
                        print "'%s' ist unter der Relation '%s' nicht zu finden!\n" % (term, relation)
                    else:
                        self.sb.remove(term)
                        print "'%s' wurde erfolgreich entfernt!\n" % term
        except:
            print "Beim Löschen des Terms ist ein Fehler aufgetreten!\n"





#****************Test****************#

if __name__ == '__main__':
    Hund = deskriptorsatz('Hund')
    Katze = deskriptorsatz('Katze')
    Tier = deskriptorsatz('Tier')
    Hund.add_relation('Saeuegetier','OB')
    Hund.add_relation('Pudel','UB')
    Hund.add_relation('Dackel','UB')
    Hund.add_relation('Hundefutter','VB')
    Hund.add_relation('Raubtier','OB')
