# -*- coding: UTF-8 -*-
# Gruppe
# Liesa Witt, Jan Simon Scheddler, Konrad Kowalke, Michael Weidauer
# Deskriptorsatz Relationen werden festgelegt

#hier wird ein Dictionary erstellt um unseren Thesaurus zu speichern
thesaurus={}
#benutzen eine dict um alle self.speicher zu speichern
all_speicher={}
def search(term):
    """
    In Funktion oder Methoden,
    bitte schreiben Kommentar in disen Bloc mit drei mal(") un eine
    Docmentation Block zu machen.
    Alle wichtige Information muessen in disen Documentation Block geschiben.

    Die Kommentar mit # nur funktioniert wir kommenta,um eine Satz zu erklaeren.
    siehen unter-->.
    """
    try:
        for ds in thesaurus.keys():
            if term in thesaurus[ds].speicher:
                #-->Ueberprufen ob das Term in self.speicher
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
            Methode collcet_speicher():
            Nach jeden Add Operator, ZB ruf add_relation,
            dann
            1.in finally Block von diesen add_relation wird
            coeect_speicher() angeruft, um self.speicher zu erneuen,
            2.und die all_tehsaurus zu erneuen.
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
        

    def add_relation(self,term,relation):
        """
        hier wird eine neue Relation in unseren Speicher eingefügt.
        Wird hier auch noch geprueft, ob die Relation bereits im
        Speicher ist?

        Ja, zuerst, ueberpruefen wir ob die relation is eine der in
        der liste aufgelisten String, bwz. ['BF','BS'...]
        Wenn ja, dann ueberpruefen wir ob das Term schon in self.speicher,
        wenn nein, dann machen wir eine Hinzufugen.

        Zuerst, wir machen relation(Argument) kleinschreiben,
        weil in __inin__, jede Eingenschaft von self ist klein
        schreiben.

        Dann wir rufe self.__dict__an, bekommt wir alle information
        von diese self in eine dict.
        Mit self.__dict__[relation], !!jetzt, die relation hier ist
        nicht die relation als Argument, sonder die relation in Agument
        nach Kleingeschreibung.

        jedes Mal wir bentuzen .append() methode un das neue Term in
        besteimmten Relation hinzufugen.

        Nach erfolgreicht Hinzufugen, mussen wir eine True return,
        aber jedes mal wir self.speicher ernenen, obwohl das erfolgricht
        hinzufuegt wurde oder nicht. Dehalb wir schreiben self.collect_speicher
        in finally block.

        Das bedeute, obwohl das erfolgrich oder nicht,
        macht ein mal collect_speicher,dann alles wird erneut.
        """
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
    d1=Deskriptorsatz('Verkehr',['Transport'],[],['Verkehr'],['Stadtverkehr'],['Verkehrspolitik'])
    T=thesaurus
    D=Deskriptorsatz
    d2=D('Verkehrspolitik',['Transport Policy'],[],['Verkehrspolitik'],['Nahverkehrspolitik'],['Verkehr'])


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
