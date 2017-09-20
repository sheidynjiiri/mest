import time


class ToothBrush:
	def __init__(self, color, toothpaste=None):
		self.color = color

	def add_toothpaste(self, toothpaste):
		self.toothpaste = toothpaste

	def brush(self, teeth, seconds):
		print("brushing...")
		time.sleep(seconds)
		print("finished brushing")


class ElectricBrush(ToothBrush):
	def __init__(self, color):
		super().__init__(self, color)
		self.__is_on = False

	def turn_on(self):
		self.__is_on = True

	def turn_off(self):
		self.__is_on = False


yellow_electric_brush = ElectricBrush('yellow')
eyram = ToothBrush('purple')
eyram.brush('brown',10)

