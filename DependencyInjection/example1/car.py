
from engine import ElectricEngine

class Car:

	def __init__(self, engine):
		self._engine = engine

	def get_engine_voice(self):
		self._engine.get_voice()


if __name__ == '__main__':

	c = Car(ElectricEngine())
	
	c.get_engine_voice()