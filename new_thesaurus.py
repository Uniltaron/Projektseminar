# -*- coding: UTF-8 -*-
# Gruppe 412
# Liesa Witt, Jan Simon Scheddler, Konrad Kowalke, Michael Weidauer
# Deskriptorsatz Relationen werden festgelegt

#hier wird ein Dictionary erstellt um unseren Thesaurus zu speichern
thesaurus={}
#benutzen eine dict um alle self.speicher zu speichern
all_speicher={}
def search(term):
    try:
        for ds in thesaurus.keys():
            if term in thesaurus[ds].speicher:
                print thesaurus[ds]
            else:
                return False
        return True
    except:
        print "Exception:\nsearch() funktion."



class Deskriptorsatz(object):
    def __init__(self,ds,bf=[],bs=[],ob=[],ub=[],vb=[],sb=[]): #an dieser Stelle wird der Deskriptorsatz initialisiert
        try:
            if not isinstance(ds,basestring):
                raise Exception()
            self.ds=ds
            self.bf=bf
            self.bs=bs
            self.ob=ob
            self.ub=ub
            self.vb=vb
            self.sb=sb
            thesaurus[ds]=self
        except:
            print"Leider Pech gehabt. Deskriptorsatz konnte nicht geladen werden"
        finally:
            self.collect_speicher()

    def __repr__(self): #hier wird eine kleine TUI ausgegeben von dem, was wir in unserem Deskriptorsatz stehen haben
        return "\n {ds}\n{line}\nBF:{bf}\nBS:{bs}\nSB:{sb}\nOB:{ob}\nUB:{ub}\nVB:{vb}\n{stars}\n".format(
            ds=self.ds, bf=self.bf, bs=self.bs,sb=self.sb,ob=self.ob,
            ub=self.ub,vb=self.vb, stars='*'*50,line='*'*50)

    def collect_speicher(self):
        '''
        was macht denn unser collect_speicher hier? 
        '''
        try:
            l=[]
            for ds in self.__dict__.keys():
                if (not ds is 'speicher') and (not ds is 'ds'):
                    l.extend(self.__dict__[ds])
            l.append(self.ds)
            all_speicher[self.ds]=l
            self.speicher=l
        except:
            print 'Exception'
        

    def add_relation(self,term,relation): #hier wird eine neue Relation in unseren Speicher eingefügt. Wird hier auch noch geprueft, ob die Relation bereits im Speicher ist?
        try:
            if ((relation in ['BF','BS','SB','OB','UB','VB'])
                and (not term in self.speicher)):
                relation=relation.lower()
                self.__dict__[relation].append(term)
                return True
            else:
                return False
        except:
            print "Exception:\nadd_relation()"
        finally:
            self.collect_speicher()

        
    
#======
#Testdeskriptorsatz fuer Testlauf
#======

if __name__ == '__main__':
    d1=Deskriptorsatz('Verkehr',['Transport'],[''],['Verkehr'],['Stadtverkehr'],['Verkehrspolitik'])
    T=thesaurus
    D=Deskriptorsatz
    d2=D('Verkehrspolitik',['Transport Policy'],[''],['Verkehrspolitik'],['Nahverkehrspolitik'],['Verkehr'])


"""
self,ds,bf=[],bs=[],ob=[],ub=[],vb=[],sb=[]

VERKEHR
--  ---------------
BF  Transport
BF  Verkehrswesen
UB  Schifffahrt 
UB  Stadtverkehr
VB  Verkehrspolitik
--  ---------------

    VERKEHRSPOLITIK
--  -------------------
BF  Transport Policy
OB  Verkehrspolitik
UB  Luftverkehrspolitik
UB  Nahverkehrspolitik
VB  Verkehr
--  -------------------
"""    
