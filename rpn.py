#!/usr/bin/env python3

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			if (token == '+'):
				arg1 = stack.pop()
				arg2 = stack.pop()
				return arg1 + arg2
			elif (token == '^'):
				arg1 = stack.pop()
				arg2 = stack.pop()
				return arg2**arg1


def main():
	while True:
		print(calculate(input('rpn calc> ')))

if __name__ == '__main__': 
    main()

