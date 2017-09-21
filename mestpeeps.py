
class Person:

	def __init__(self, name, nationality):
		self.name=name
		self.nationality=nationality


class EIT(Person):

	def __init__(self, name, nationality, fun_facts):
		super().__init__(name, nationality)
		self.fun_facts=fun_facts

	def __repr__(self):
		return """
		Name: {}
		Nationality: {}
		Fun_facts: {}
		""".format(self.name, self.nationality, self.fun_facts)                                 #finish solution


class Fellow(Person):
	num_of_fellows = 0

	def __init__(self, name, nationality, happiness_level=0):
		if Fellow.num_of_fellows < 4:
			super().__init__(name, nationality)
			self.happiness_level=happiness_level
			Fellow.num_of_fellows += 1
		else:
			print("we can not afford to hire {}!".format(name))

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
	def __init__(self, eit_l=[], f_list=[]):
		self.eit_l = eit_l
		self.f_list = f_list

	def new_eit(self, eit):
		if isinstance(eit, EIT):
			self.eit_l.append(eit)

		else:
			print("not an eit.")

	def new_fellow(self, fellow):
		if isinstance(fellow, Fellow):
			self.f_list.append(fellow)
		else:
			print("not a fellow")


	def __repr__(self):
		return("no of eits: {} \t no of fellows: {}".format(len(self.eit_l), len(self.f_list)))


# MEST=School()
# MEST.new_eit(EIT("Njiiri", "Kenyan", "python humbles me"))
# MEST.new_fellow(Fellow("Andrew", "American", 4))
# print (MEST)

fellows = Fellow("Edem", "Ghana", 5)
fellows = Fellow("Edem", "Ghana", 5)
fellows = Fellow("Edem", "Ghana", 5)
fellows = Fellow("Edem", "Ghana", 5)
fellows = Fellow("Edem", "Ghana", 5)
fellows = Fellow("Edem", "Ghana", 5)


print(Fellow.num_of_fellows)


