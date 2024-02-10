#Execution order

print('line 1') # this will also be ignored.
print('line 2')
print('line 3')

#data types
print('words')
print("words")
print(123) # integers / ints
print(-10)
print(1.5) # floating point value / float

#operations 
print(3 + 3)
print(3 - 3)
print(3 / 3) # -> 1.0
print(3 * 3) 
print(10 + 0.12131313515) # -> 10.12131313515 #we can sum ints and floats

#?--- we can't sum numbers + strings --- 
print(10 * 'hello') #! -> error

#?---  but we actually can multiply numbers * strings  ---
print(10 * 'hello') #* -> hellohellohellohellohellohellohellohellohellohello

#for operations It just follows the math rules:
print(13 - 3 * 4 + 2) #* --> 3
print(13 - 3 * (4 + 2)) #* --> +5

#? -------- Variables ----------

test = 123
print(test + 10) #* --> 133 

test += 50 #* Equals to --> test = test + 50 

print(test) #* --> 173 


# Some limitations:

#! Mandatory : 

#! only letters -> A-z, numbers -> 0-9 and  _
#! cannot start with a number -> (1test is invalid)
#! case sensitive -> ( test123 is different from Test123 )
#! we cannot use reserved words (like "print", for instance)

#* It would be beneficial to use: 

#* use understandable names
#* use snake_case


# Input 


input_prompt = input("cuanto es 50 topitos + 50 topitos?:")
print(input_prompt)



#*----------  Containers -----------

#? ------ Tuple -----------  
Tuple = ('bob', 123, 'Lisa', ('another list'))

#? ------ List ----------- 
List = ['bob', 123, 'Lisa', ('another list')]

# () or [] and then comma separated values
# a tuple cannot change (immutable) while you can change the values of a list 

#? ------ Set -----------
Set = {1,2,3,'test'}
#Every entry is unique (it's not key/value pair)

#? ------ Dictionary -----------
Dictionary = {'name':'Bob',123:'test','Lisa':(123)}
#Key:value pairs instead of single entries

