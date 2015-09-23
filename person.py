import os 
from grid import *	

class Person():
	def move(self,letter,grid,val): #enables movement of player on the screen and also of donkey and fireballs.
			grid.printchar(self.x,self.y,self.next)
			x=self.x
			y=self.y
			if letter == 'P':
					if val == 'd' and self.move_right(grid,self.x,self.y) == True:
						self.next = grid.getchar(x,y+1)
						self.y = self.y+1
					elif val == 'a' and self.move_left(grid,self.x,self.y) == True:
						print "Entered left"
						self.next = grid.getchar(x,y-1)
						self.y = self.y-1
					elif val == 'w' and self.move_up(grid,self.x,self.y) == True:#grid.getchar(x-1,y) == 'H' or grid.getchar(x,y) == 'H':
						self.next = grid.getchar(x-1,y)
						self.x = self.x-1
					elif val == 's' and self.move_down(grid,self.x,self.y) == True:
						self.next = grid.getchar(x+1,y)
						self.x = self.x+1

			grid.printchar(self.x,self.y,'P')

	def checkwall(self,grid): #checks wall position.
		if grid.getchar(x,y+1) == 'X' or grid.getchar(x,y-1) == "X":
			return True
		return False

	def move_left(self,grid,x,y):
		if grid.getchar(x,y-1) == 'X' or grid.getchar(x+1,y-1) == ' ':
			return False
		return True

	def move_right(self,grid,x,y):
		if grid.getchar(x,y+1) == 'X' or grid.getchar(x+1,y+1) == ' ':
			return False
		return True

	def move_up(self,grid,x,y):
		if grid.getchar(x-1,y) == ' ' and grid.getchar(x,y+1) == 'X':
			return True
		elif grid.getchar(x-1,y) == ' ':
			return False
		return True

	def move_down(self,grid,x,y):
		if grid.getchar(x+1,y) =='X' or grid.getchar(x+1,y) == ' ':
			return False
		return True

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y