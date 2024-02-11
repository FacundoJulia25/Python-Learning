# # a basic class

# class Person:
#     name = 'Random'
#     age = 48
#     address = 59
#     lp = 100

#     def completeUser(self, user_archivo):
#         user_name, user_age, user_address, user_lp = user_archivo
#         print(user_archivo)
#         self.name = user_name
#         self.age = user_age
#         self.address = user_address
#         self.lp = user_lp


# # create an instance
# archivo_lucas = ('Lucas', 21,'Av. Siempre viva', 100)

# Lucas = Person()
# Lucas.completeUser(user_archivo = archivo_lucas)
# print(Lucas.age)

#? Dunder Methods: 
# # Mage class
# class Mage: 
#     def __init__(self, health, mana):
#         self.health = health
#         self.mana = mana
    
#         print('Mage class was created') 
#     def attack(self, target):
#         target.health -= 10

# class Monster():
#     health = 40


# easy_monster = Monster()
# dark_magician = Mage(health=240,mana= 300)

# print('this is the health of the monster before: ',easy_monster.health)
# dark_magician.attack(easy_monster)
# print('this is the health of the monster after: ',easy_monster.health)

#? inheritance 
# class Human:
#     def __init__(self, health):
#         self.health = health
        
#     def attack(self):
#         print('attack')

# class Warrior(Human):
#     def __init__(self, health, defense):
#         super().__init__(health)
#         self.defense = defense
#         print('Warrior was created')

# class Barbarian(Human):
#     def __init__(self, health, damage):
#         super().__init__(health)
#         self.damage = damage
#         print('Barbarian was created')

   

# warrior_1 = Warrior(100, 1500)
# barbarian_1 = Barbarian(200,  2000)

# print(warrior_1.defense, warrior_1.health )
# print(barbarian_1.damage, barbarian_1.health)

#exercise 
# class Criatures:
#     def attack(self):
#         print(f'attack:{self.damage}')

# class Monster(Criatures):
#     def __init__(self, health, damage):
#         self.health = health
#         self.damage = damage

#     def __str__(self):
#         return f'A monster with {self.health} HP'

# lil_monster = Monster(1500, 300)
# lil_monster.attack()

# print(lil_monster)