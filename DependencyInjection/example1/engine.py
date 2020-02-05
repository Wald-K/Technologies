from abc import ABC, abstractmethod

class Engine(ABC):

	@abstractmethod
	def get_voice(self):
		pass

	@abstractmethod
	def get_price(self):
		pass




class ElectricEngine(Engine):
	def get_voice(self):
		print('silent engine')

