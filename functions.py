# create a function 

def print_x_times(word, num = 5):
    counter = 0
    while counter <= num: 
        print(word,counter)
        counter +=1

#call
print_x_times('conteo numero:')


# pythagoras theorem

def hypotenuse_calculator(side_a, side_b):
    hypotenuse = (side_a **2 + pow(side_b, 2)) ** (1/2)
    print('the hypotenuse is: ', round(hypotenuse, 2))

hypotenuse_calculator(1, 1)