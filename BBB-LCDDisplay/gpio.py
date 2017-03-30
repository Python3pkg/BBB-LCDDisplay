import os
from utils import *

class BBB_GPIO:
	def __init__(self, pin):
		print(pin)
		self.pin = self.__convert_pin(pin)
		self.gpio_path ='/sys/class/gpio/'
		self.pin_path = '{0}{1}/'.format(self.gpio_path, self.pin)
		self.__create()

	def __convert_pin(self, pin):
		try:
			return eval(pin)
		except NameError:
			print('Bad pin. Please choose an other!')

	def __open_directory(self, directory):
		os.chdir(directory)

	def __cmd(self, arg, files):
		os.system('sudo echo {0} > {1}'.format(arg, files))

	def __create(self):
		self.__open_directory(self.gpio_path)
		self.__cmd(self.pin[4:], 'export')

	def remove(self):
		self.__open_directory(self.gpio_path)
		self.__cmd(self.pin[4:], 'unexport')

	def value(self, value):
		self.__open_directory(self.pin_path)
		if eval(str(value)) == '1' or '0':
			self.__cmd(eval(str(value)), 'value')
		else:
			raise Exception('Incorrect value, try with HIGH or LOW!')

	def direction(self, direction):
		self.__open_directory(self.pin_path)
		if direction == 'out' or 'in':
			self.__cmd(direction, 'direction')
		else:
			raise Exception('Incorrect direction, try with OUTPUT or INPUT')
