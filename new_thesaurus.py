#
#
#
#

thesaurus={}
thesaurus['Speicher'] =[]

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
            thesaurus[ds]=self
        except:
            print"Ja, Pech gehabt. Deskriptorsatz konnte nicht geladen werden"

    def __repr__(self):
        return "\n   {ds}\n{line}\nBF:{bf}\nBS:{bs}\nSB:{sb}\nOB:{ob}\nUB:{ub}\nVB:{vb}\n{stars}\n".format(ds=self.ds, bf=self.bf, bs=self.bs,sb=self.sb,ob=self.ob,ub=self.ub,vb=self.vb, stars='°'*50,line='+'*50)

    def speicher(self):
	   try:
		  data=[]
		  for key in self.__dict__.key():
		      data.extend(self.__dict__[key])
		  thesaurus['Speicher'].extend(data)
	   except:
	       print"Problem bei der Speichermetode"
#======
#Test
#======
			
if __name__ == '__main__':
    d1=Deskriptorsatz('Hund')

    
