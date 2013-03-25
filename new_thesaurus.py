#
#
#
#d

#benutzen eine dict un alle Dskriptorsatz zu speichern
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
    def __init__(self,ds,bf=[],bs=[],ob=[],ub=[],vb=[],sb=[]):
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
            print"Ja, Pech gehabt. Deskriptorsatz konnte nicht geladen werden"
        finally:
            self.collect_speicher()

    def __repr__(self):
        return "\n {ds}\n{line}\nBF:{bf}\nBS:{bs}\nSB:{sb}\nOB:{ob}\nUB:{ub}\nVB:{vb}\n{stars}\n".format(
            ds=self.ds, bf=self.bf, bs=self.bs,sb=self.sb,ob=self.ob,
            ub=self.ub,vb=self.vb, stars='+'*50,line='+'*50)

    def collect_speicher(self):
        '''
        usg:xxxxx
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
#Test
#======

if __name__ == '__main__':
    d1=Deskriptorsatz('Hund',['BBC'],['CNN'])
    T=thesaurus
    D=Deskriptorsatz
    d2=D('BBC')
    d3=D('CNN',['BBC'])

    
