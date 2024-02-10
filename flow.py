
#? ----- If statement -------

# if 5 < 4:
#     print('correct mi loco')
# elif 5>6:
#     print('vo me ta cargando?')
# elif 6>5:
#     if len([2,2,3]) > 2:
#         print('list is long enough')
# else:
#     print('incorrect result') 


#? ----- While loop -------

# counter = 0

# while counter <= 10:
#     print(counter)
#     counter+=1
#     if counter == 5:
#         print('counter is 5')
# print('while loop has finished!')

#?------- for loop --------

# test_list = {"uno":1,6:"2",2:3,4:"4 es capo",5:5}
# for x in test_list.keys(): 
#     print(x)
# # => you receive
# # uno
# # 6
# # 2
# # 4
# # 5
    
# for x in test_list.values(): 
#     print(x) 
# # => you are receiving
# # 1
# # 2
# # 3
# # 4 es capo
# # 5

# for x in test_list.items(): 
#     print(x)
# # => you are receiving
# # (6, '2')
# # (2, 3)
# # (4, '4 es capo')
# # (5, 5)

# for k,v in test_list.items():
#     print(k)
#     print(v)


#? ------- Truthy and falsy --------
# if 0:
#     print('something')

# #here we don't have anything because in python
# # Are falsy #!=> empty containers: {},[],(), empty strings:"" and 0
# # Everything else is:
# #           #* => Truthy

#exercise 

# list = (1,2,3,4,5) 
# counter=0
# for x in list:
#     if x == 2:
#         print('the value is 2')
#     else:
#         print('the value is not 2')
# while counter <=5:
#         print('last item')
#         counter+=1