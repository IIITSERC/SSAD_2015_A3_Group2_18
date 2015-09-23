from Person import *
import random
from grid import *
from main import *
#Incomplete Function, thus unused in the game. Attempted to create fireball obstacles.
class fireballs(Person):
	def fireball(self):
		l = []
		i = random.randint(0,30)
		j = random.randint(0,80)  