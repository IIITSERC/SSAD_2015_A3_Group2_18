from person import *
#This is the player's position initiaization. And the declaration of Player class.
class Player(Person):#inherits from Person class.
	def __init__(self):
		self.x = 28
		self.y = 1
		self.next = ' '