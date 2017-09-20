class EIT:
	def __init__(self, name, nationality, fun_facts):
		self.name=name
		self.nationality=nationality
		self.fun_facts=fun_facts

	def __repr__(self):
		return """
		Name: {}
		Nationality: {}
		Fun_facts: {}
		""".format(self.name, self.nationality, self.fun_facts)


class fellows:
	def __init__(self, name, nationality, happiness_level, eat, teach):
		self.name=name
		self.nationality=nationality
		self.happiness_level=happiness_level
		self.eat=eat
		self.teach=teach

	def __repr__(self):
		return """
		Name: {}
		Nationality: {}
		Happiness_level: {}
		Eat: {}
		Teach: {}
		""".format(self.name, self.nationality, self.happiness_level, self.eat, self.teach)


class School:
	def __init__(self,eit, fellow):
		self.eit=eit
		self.fellow=fellow

	def new_eit(self,eit):
		self.eit.append(eit)

	def new_fellow(self,fellow):
		self.fellow.append(fellow)


MEST=School()
MEST.new_eit(eit("Njiiri", "Nationality", "python humbles me"), fellow("Andrew", "American", "happy", "vegetables", "humour"))
print (MEST)




