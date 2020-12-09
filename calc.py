import sympy
from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
def main():
	while True:
		print('Select the operator you would like to use.')
		print(" (1) Addition\n (2) Subtraction\n (3) Multiplication\n (4) Division")

		selectOP = input()
		if selectOP in ('1','2','3','4','5'):
			break
		else:
			print("oops, please enter a valid number")

	#Addition
	if selectOP == ('1'):
		print("select your first number.")
		ADDnum1 = int(input())
		print("select your second number.")
		ADDnum2 = int(input())
		print(ADDnum1 , 'plus' ,  ADDnum2 ,  'is' ,  ADDnum1 + ADDnum2)

	#Subtraction
	if selectOP == ('2'):
		print("select your first number.")
		SUBnum1 = int(input())
		print("select your second number.")
		SUBnum2 = int(input())
		print(SUBnum1 , 'subtracted by' , SUBnum2 , 'is' , SUBnum1 - SUBnum2)

	#Multiplication
	if selectOP == ('3'):
		print("select your first number.")
		MULnum1 = int(input())
		print("select your second number.")
		MULnum2 = int(input())
		print(MULnum1 , 'multiplied by' ,  MULnum2 , 'is' , MULnum1 * MULnum2)

	#Division
	if selectOP == ('4'):
		print("select your first number.")
		DIVnum1 = int(input())
		print("select your second number.")
		DIVnum2 = int(input())
		print(DIVnum1 , 'divided by' , DIVnum2 , 'is' , DIVnum1 / DIVnum2)

	#simplifacation? im bad at spelling
	if selectOP == ('5'):
		print("what equation would you like to simplify?")
		SIM = (input())
		SIMans = (sympy.simplify(SIM))
		print(SIMans)


	while True:
			answer = input('Do you want to continue?:')
			if answer.lower().startswith("y"):
				print("ok, carry on then")
				main()
			elif answer.lower().startswith("n"):
				print("sayonara, Robocop")
				exit()

main()
