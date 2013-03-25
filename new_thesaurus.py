#
#
#
#d
thesaurus={}
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
            self.speicher=[]
            self.collect_speicher()
            thesaurus[ds]=self
        except:
            print"Ja, Pech gehabt. Deskriptorsatz konnte nicht geladen werden"

    def __repr__(self):
        return "\n {ds}\n{line}\nBF:{bf}\nBS:{bs}\nSB:{sb}\nOB:{ob}\nUB:{ub}\nVB:{vb}\n{stars}\n".format(ds=self.ds, bf=self.bf, bs=self.bs,sb=self.sb,ob=self.ob,ub=self.ub,vb=self.vb, stars='°'*50,line='+'*50)

    def collect_speicher(self):
        
        '''
        usg:xxxxx
        
            
        '''
        try:
            l=[]
            for ds in self.__dict__.keys():
                if (ds is 'speicher'):
                    if isinstance(self.__dict__[ds],basestring):
                        l.append(self.__dict__[ds])
                    elif isinstance(self.__dict__[ds],list):
                        l.extend(self.__dict__[ds])
                    self.speicher=l
                return True
        except:
            print 'Exception'
            return False
        

    def add_relation(self,term,relation):
        try:
            if (not isinstance(term,basestring)) and (not isinstance(relation,basestring)):
                raise Exception()
            else:
                if relation is 'BS':
                    self.bs.append(term)
                    self.collect_speicher()
                    return True
            
        except:
            print 'Exception:add_relation()'
            return False

    
#======
#Test
#======

if __name__ == '__main__':
    d1=Deskriptorsatz('Hund')
    T=thesaurus
    D=Deskriptorsatz

    
