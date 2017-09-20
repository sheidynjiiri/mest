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
		""".format(self.name, self.nationality, self.fun_facts)                                 #finish solution


class Fellow:
	def __init__(self, name, nationality, happiness_level=0):
		self.name=name
		self.nationality=nationality
		self.happiness_level=happiness_level

	def eat(self):
		self.happiness_level += 1

	def teach(self):
		self.happiness_level -= 1

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


MEST=School()
MEST.new_eit(eit("Njiiri", "Nationality", "python humbles me"), fellow("Andrew", "American", "happy", "vegetables", "humour"))
print (MEST)




