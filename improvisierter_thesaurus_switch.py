class Thes(object):
	def __init__(self, name, bs=[], bf=[], ub=[], ob=[], sb =[]):
		self.name = name
		self.bs = bs
		self.bf = bf
		self.ub = ub
		self.ob = ob
		self.sb = sb
	
	def add_relation(self, begriff, relation):
		# was ist das tollste an Dictionarys? Genau! Man kann jeden Mist hineinspeichern!
		# Also speichern wir einfach die gewuenschte Relation ab und basteln uns einen improvisierten Switch...
		improvised_switch = {"bs":self.bs,"bf":self.bf,"ub":self.ub,"ob":self.ob,"sb":self.sb}
		if begriff in improvised_switch[relation]:
			print "Gibt es schon!"
			return False
		improvised_switch[relation].append(begriff)
		return True

t = Thes("Hallo")
print t.name
print t.bf

t.add_relation("Hi","bf")
print t.bf