from grid import *
from player import *
import os
def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch
#Main function that should be run.
def main():
	sc=Screen()
	P = Player()#Creates object of Player class.
	sc.collect_coins()#calls collect_coins function.
	sc.printScreen()
	while 1: 
		print "Enter move: a/d/w/s:",
		val = getchar()
		if val == 'q':
			os.system("clear")
			print "Bye"
			break
		P.move('P',sc,val)#calls move() for player.
		print ""
		os.system("clear")
		sc.printScreen()
		if P.get_x() == 1:
			sc.add_score()
			print "You Won!! Yayyy :) Your score is: "+ str(sc.return_score())
			print "Okay Bye! :)"
			break

if __name__=="__main__":
	main()