# -*- coding: utf-8 -*-
class Katze(object):
    alle_katzen = {}
    
    def __init__(self,name,relations_str):
        self.name = name
        self.verwandte = {}
        Katze.alle_katzen[name] = self
        
        for verwandschaftsgrad,namen in relations_str.iteritems():
            self.verwandte[verwandschaftsgrad] = []
            for name in namen:
                print name, verwandschaftsgrad
                self.verwandte[verwandschaftsgrad].append(self.return_cat(name))
                
    def return_cat(self,name):
        if not name in Katze.alle_katzen: 
            Katze.alle_katzen[name] = Katze(name,{})
        return Katze.alle_katzen[name]

Katze('Minka',{'Schwester':['Uschi','Andere Katze'],'Vater':['Paul'],'Omma':['Ommakatze']})
Katze('Uschi',{'Schwester':['Minka','Andere Katze']})

print Katze.alle_katzen['Minka'].verwandte["Schwester"][0].name
print Katze.alle_katzen['Uschi'].verwandte
