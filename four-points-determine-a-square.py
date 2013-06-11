#Programming Praxis - Four Points Determine A Square
#Solution by Meenakshi Madan

"""
Today's exercise is an interview question. It's not hard, but it's unusual enough that it took several minutes before I knew what to do.

Consider a list of four points on a plane; the points have integral coordinates, and their order is irrelevant. The four points determine a square if the distances between them are all equal, and the lengths of the two diagonals are also equal. For instance, the following lists are all squares:

(0,0), (0,1), (1,1), (1,0) -- the unit square
(0,0), (2,1), (3,-1), (1, -2) -- square not aligned to axis
(0,0), (1,1), (0,1), (1,0) -- unit square, in different order

And the following lists do not represent squares:

(0,0), (0,2), (3,2), (3,0) -- rectangle
(0,0), (3,4), (8,4), (5,0) -- rhombus
(0,0), (0,0), (1,1), (0,0) -- degenerate
(0,0), (0,0), (1,0), (0,1) -- degenerate

The degenerate square that consists of four repetitions of a single point may be considered either square, or not.

Your task is to write a function that determines if four input points determine a square.

"""


import sys
from math import sqrt

def get_coords():
  #user_input = raw_input("Enter a list of points. For example (0,0) (0,1) (1,1) (1,0)\n")
	print "Enter a list of points. For example (0,0), (0,1), (1,1), (1,0)"
	points = raw_input()
	try:
		#return literal_eval('(' + strs.replace(' ',',') +')')
		return ast.literal_eval(points)
	except SyntaxError:
		print "Please enter the coordinates in the format mentioned"
		exit()
		
		
#print get_coords()


def is_square(coords):
	if len(coords) != 4:
		return False
	else:
		side, diag = [0, 0], [0, 0]
		for i in range(1, 4):
			#print side, diag
			j=i-1
			while j>=0:
				#print side, diag
				x = coords[i][0] - coords[j][0]
				y = coords[i][1] - coords[j][1]
				d = sqrt(x*x + y*y)
				#print d
				j -= 1
				if i ==1:
					side = [d, 1]
				elif d == side[0]:
					side[1] += 1
					continue
				elif d == sqrt(2) * side[0]:
					diag[0] = d
					diag[1] += 1
					continue
				elif side[0] == sqrt(2) * d:
					side, diag = diag, side
					side[0] = d
					side[1] += 1
					continue
				else:
					return False
		#print side, diag
		if side[1] == 4 and diag[1] == 2:
			return True
	return False
			
		
		
print is_square(get_coords())
	
