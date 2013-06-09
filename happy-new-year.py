"""
Problem statement:
As we begin the new year, we note that 109-8*7+654*3-2/1 = 2013. There are three other combinations of the numbers 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, in order, combined with the five operators NIL, +, -, * and / that also evaluate to 2013.

Your task is to write a program that finds all four expressions that evaluate to 2013.

"""

import itertools
operands = [str(i) for i in reversed(range(1, 11))]
operators = ['', '+', '-', '/', '*']

for seq in list(itertools.product(operators, repeat=9)):
  exp = ''
	for i in range(9):
		exp += operands[i] + seq[i]
	exp += operands[9]
	if eval(exp) == 2013:
		print exp
