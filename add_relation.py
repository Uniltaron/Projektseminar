def add_relation (self,term,relation):
	
	if (term.BS): #Überprüfen, ob der Term ein Nichtdeskriptor ist
		return "Bei dem Term handelt es sich um einen Nichtdeskriptor!"
	
	elif (self == term): #Überprüfen, ob der Eintrag und der Term gleich sind
		return "Ein Eintrag kann sich nicht selbst als Relation haben!"
		
	elif ():
	
	
	
	
	
	
	
	
	else:
	
		if (relation == BS): #Hinzufügen einer Relation BS
			if (self.OB or self.UB or self.BF or self.VB) #hat der Eintrag bereits andere Relationen kann er kein BS erhalten
				return "Bei dem Eintrag handelt es sich um einen Deskriptor! Er kann daher kein Nichtdeskriptor sein!"
			else: 
				self.BS.append(term) #Füge dem Eintrag unter BS den Term hinzu
				term.BF.append(self) #Füge dem Term unter BF den Eintrag hinzu
			
		elif (relation == BF): #Hinzufügen einer Relation BF
			if (term.OB or term.UB or term.BF or term.VB): #hat der Term bereits andere Relationen kann er kein BF enthalten
				return "Bei dem Term handelt es sich um einen Deskriptor! Er kann daher kein Nichtdeskriptor sein!"
			else:
				self.BF.append(term) #Füge dem Eintrag unter BF den Term hinzu
				term.BS.append(self) #Füge dem Term unter BS den Eintrag hinzu
		
		elif (relation == VB): #Hinzufügen einer Realtion VB
			self.VB.append(term) #Füge dem Eintrag unter VB den Term hinzu
			term.VB.append(self) #Füge dem Term unter VB den Eintrag hinzu
			
		elif (relation == OB): #Hinzufügen einer Relation OB
			if (self.UB == term): #Ist der neue Oberbegriff bereits der Unterbegriff des Eintrags?
				return "Der Unterbegriff eines Eintrags kann nicht dessen Oberbegriff sein!"
			elif (self.OB): #Überprüfen, ob der Eintrag bereits einen Oberbegriff hat
				return "Der Eintrag hat bereits einen Oberbegriff!"
			else:
				self.OB.append(term) #Füge dem Eintrag unter OB den Term hinzu
				term.UB.append(self) #Füge dem Term unter UB den Eintrag hinzu
				
		elif (relation == UB): #Hinzufügen einer Relation UB
			if (self.OB == term): #Ist der neue Unterbegriff bereits der Oberbegriff des Eintrags?
				return "Der Oberbegriff eines Eintrags kann nicht dessen Unterbegriff sein!"
			elif (self.UB): #Überprüfen, ob der Eintrag bereits einen Unterbegriff hat
				return "Der Eintrag hat bereits einen Unterbegriff!"
			else:
				self.UB.append(term) #Füge dem Eintrag unter OB den Term hinzu
				term.OB.append(self) #Füge dem Term unter UB den Eintrag hinzu