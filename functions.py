# create a function 

# def print_x_times(word, num = 5):
#     counter = 0
#     while counter <= num: 
#         print(word,counter)
#         counter +=1

# #call
# print_x_times('conteo numero:')


# # pythagoras theorem

# def hypotenuse_calculator(side_a, side_b):
#     hypotenuse = (side_a **2 + pow(side_b, 2)) ** (1/2)
#     print('the hypotenuse is: ', round(hypotenuse, 2))

# hypotenuse_calculator(1, 1)

# # exercise: 
#* create a "shouter" function that takes 2 arguments:
#- A string and a number

# The function should:
# #*- Print the string multiple times (whatever is specified in the number argument.)
# #*- If the number is greater than 10 don't print 
# the input string. instead, print 'you are too loud' once
# #*-the function should also return the string 'done' and have default values

## code goes here:

def shouter(string ='pum', number=1):
    if number > 10:
        print('you are too loud')
    else:    
            for i in range(number):
                print(string.upper())
    return 'done'

status = shouter("test", 5)
print(status)
