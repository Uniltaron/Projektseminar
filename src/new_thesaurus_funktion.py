def __init__(self, name, bs=[], bf=[], ub=[], ob=[], sb =[]):
	self.name = name
	self.bs = bs
	self.bf = bf
	self.ub = ub
	self.ob = ob
	self.sb = sb
	thesaurus[name] = self
	self.collect_relations()
	
def __collect_relations__(self):
	for ds in self.ob:
		if (not thesaurus.has_key(ds)):
			ds = deskriptorsatz(ds,bs, bf, self.name,[],[])
	for ds in self.ub:
		if (not thesaurus.has_key(ds)):
			ds = deskriptorsatz(ds,bs, bf, [],self.name,[])