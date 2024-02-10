# Excercise 1 greeting app

#print('Hey :)')
#print("what's your name dude? ")
#user_name = input()

#print('Hello', user_name, 'nice to meet you :D' )

# exercise number 2:
# create a pythagoras theorem calculator 
# Once it is run, the code should ask the user for 
# 2 numbers that are the width and heihgt of a triangle

#? It should output the length of the hypotenuse.

#* code from here:


print("I'm gonna ask you for 2 numbers :)")

num1 = int(input("number 1:"))
num2 = int(input("number 2:"))

# Here we have 3 considerations: 
#* 1: you can have the power of a number by doing ** "x"
#* 2: you can use the pow(number) function that accepts the number and the power you want to have 
#* 3: you can get the root of a number by multiplying powering It for 1/2 

hypotenuse = (num1 ** 2 + pow(num2, 2)) ** (1/2)

print('This is your hypotenuse:', round(hypotenuse, 2))