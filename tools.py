
#? f strings  
# user_age = 10
# user_name = 'Petter'
# user_information_bad_approach = user_name + ' is ' + str(user_age) + ' years old'
# user_information_f_strings = f'{user_name} is {user_age} years old. F'
# print(user_information_f_strings)
# print(user_information_bad_approach)


#? single line if statements 
# user_age = 40
# user_name = 'Anna'
# user_status = ''

# # #! bad use:
# # if user_age >= 18:
# #     user_status = 'adult'
# # else:
# #     user_status = 'child'

# #* good use: 
# user_status = 'adult' if user_age >= 18 else 'child'
# user = f'{user_name} is a {user_age} years old {user_status}'
# print(user)

#? list comprehension
# simple_list = [i*2  for i in range(0, 11, 1)]
# datas={'krilin':5, 'Vegeta':8, 'goku': 10, 'gohan ssj2': 12}
# complex_list = [f'{character} ki: {datas[character] * i} ' for i in range(1, 11, 1) for character in datas] 
# for i in range(0,10,1):
#     simple_list.append(i)

#? lambda functions 

#it's similar to an arrow functin but it's not.
#e.g let's say we want to do the next with a shorter form:
def doubleNumber(num):
    return num*2
print(doubleNumber(2))

# ok to do so we can use the lambda function:
# num_doubled = lambda num : num*2
# print(num_doubled(3))

#the ":" could be treated as a "=>" so then its returning the number multiplied
#*but that's not a great way to use It.
#There are some function that need arguments:

# random_list= [80, 40, 60, 20, 14, 77, 22]
# sorted_list = sorted(random_list)
# print(sorted_list)

#* Now a function that needs an argument:

# random_list = (("paul", 40),("laura", 50),("Stephen", 33),("sandra", 24))
# sorted_list = sorted(random_list, key = lambda user_tuple : user_tuple[1])

# print(sorted_list)

# todo Exercise:

vocals = ('A','B','C','D','E')
numbers= list(range(1,6,1))

#! this was my solution
# battleshipList = [f'{i}:{n}' for i in vocals for n in numbers]
# #now we need to use lambda function to remove the C:3
# aux_battleshipList = [f'{i}' for i in battleshipList if i != 'C:3']

#* this was the right one:
# battleshipList = [f'{i}:{num}' for i in vocals for num in numbers if f'{i}:{num}' != 'C:3']
# print(battleshipList) 
