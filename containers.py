# a_tuple = (1,2,3,'a string')

# a_list = [1,2,3,'a string']
# print(a_tuple)
# a_list.append('another word')
# print(a_list)

# a_set = {1,2,3,4} # --> {1,2,3,4}
# a_set = {1,2,3,4,4} # --> {1,2,3,4}
# #this one won't repeat the values ! 
# # It can be really useful in some cases! 
# # let's see an example: 

# a_list = [1,2,3,'a string', 2]
# print(a_list)

# #* We use the "set" function to convert the list into a set! 

# print(set(a_list)) # -> {1,2,3,'a string'}

# #* Then if we want to just get the list again can do:
# print(list(set(a_list))) # -> [1,2,3,'a string']

# a_dictionary={'key':'value', 123: [1,2,3]}


# #? ---- how to get values from a container -----

# user_list = ['Lisa','Bob','Alex','Anna','John','Zara','Mivhael','Kevin']
# print(user_list[1:6:4])

# user_list = ('Lisa','Bob','Alex','Anna','John','Zara','Mivhael','Kevin')
# print(user_list[1:6:4])

# print(a_dictionary[123])
exercise_list1 = [1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,76,86,96,160]
# voy a buscar 4 - 9 - 44
print(exercise_list1[3:14:5])
exercise_list = [1,2,3,4,5,6,7,8,9,10]

#ahora al reves 
print(exercise_list[7:0:-2])
