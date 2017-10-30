# Copyright 2017 nv314961@bu.edu
import math

class Particle(object):
	def __init__(self, label, xpos, ypos, xvel, yvel):
		self.label = label
		self.x = xpos
		self.y = ypos
		self.vx = xvel
		self.vy = yvel
	
	def __repr__(self):
		return (self.label, self.x, self.y, self.vx, self.vy)

# Computes distance between two particles
def dist(A, B):
	return math.sqrt((A.x - B.x)**2 + (A.y - B.y)**2)
	
# Collision Detect
def checkCollide(A, B):
	if(dist(A, B) <= 10):
		return True
	else:
		return False

# Update position at t = x
def move(A, t):
	A.x = A.x + t*A.vx
	A.y = A.y + t*A.vy
	
def main():
	A = Particle("3FyX3", 20, 0, -2, 1)
	B = Particle("9DndK", 0, 0, 2, 1)

	move(A, 5)
	print(A)
	# A & B will collide at t = 5

if __name__=="__main__":
	main()
#def collides(x1