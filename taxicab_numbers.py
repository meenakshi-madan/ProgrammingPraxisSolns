"""
http://programmingpraxis.com/2012/11/09/taxicab-numbers/
We haven’t done a coding interview question for a while. Here’s one that is supposedly asked at Google:

The mathematician G. H. Hardy was on his way to visit his collaborator Srinivasa Ramanujan who was in the hospital. Hardy remarked to Ramanujan that he traveled in a taxi cab with license plate 1729, which seemed a dull number. To this, Ramanujan replied that 1729 was a very interesting number — it was the smallest number expressible as the sum of cubes of two numbers in two different ways. Indeed, 103 + 93 = 123 + 13 = 1729.

Given an arbitrary positive integer, how would you determine if it can be expressed as a sum of two cubes?

Your task is to write a function that returns all the ways a number can be written as the sum of two non-negative cubes; use it to verify the truth of Ramanujan’s statement. 
"""

from math import ceil

def main():
  try:
		num = int(raw_input("Enter any integer\n"))
	except:
		print "No no that's not an integer"
		exit(1)
		
	limit = int(ceil(num ** (1/3.0)) - 1)
	possibilities = []
	
	for i in range(1, limit + 1):
		for j in range(i, limit + 1):
			if (i ** 3 + j ** 3) == num: possibilities.append((i,j))
			
	return possibilities
			
			
print main()
