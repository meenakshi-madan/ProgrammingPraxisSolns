#Programming Praxis - RPN Calculator
#Solution by Meenakshi Madan
"""Implement an RPN calculator that takes an expression like 19 2.14 + 4.5 2 4.3 / - * which is usually expressed as (19 + 2.14) * (4.5 - 2 / 4.3) and responds with 85.2974. The program should read expressions from standard input and print the top of the stack to standard output when a newline is encountered. The program should retain the state of the operand stack between expressions."""

operators = "+-/%*"
exp_stack = []

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

exp = raw_input("Enter the expression to be calculated\n").split(' ')

for term in exp:
  if is_number(term):
		exp_stack.append(term)
	elif term in operators:
		try:
			op2 = exp_stack.pop()
			op1 = exp_stack.pop()
			exp_stack.append(eval(str(op1) + term + str(op2)))
		except:
			print "Not enough operands. Please check your expression."
			exit()
	else:
		print "Invalid operators. Please check your expression."
		exit()
		
		
print exp_stack[0]
		
