
#TOPIC: 4.1 Pizzas
favorite_pizzas = ['Hawain', 'Macaroni', 'Cheeze']

# for pizza in favorite_pizzas:
#     ##print(f'I like {pizza} pizza')
# ##print('I really love pizza')

#TOPIC: 4.2 Animals
birds = ['Philippine Eagle', 'Bald Eagle', 'Hawk']

# for bird in birds:
#     ##print(f'{bird} are fearless')

#TOPIC: list of numbers using range() function

# for numbers in list(range(1, 21)):
#     ##print(numbers)
# numbers = list(range(1, 21))

# for number in numbers:
#     modified_value = number**2
#     ##print(modified_value)

# squares = []
# for value in range(1, 10):
#     number_in_squares = value ** 2
#     squares.append(number_in_squares)

# ##print(squares)
# ##print(min(squares))
# ##print(max(squares))
# ##print(sum(squares))


#TOPIC: List comprehensions
squares = [values**2 for values in range(1, 10)]
###print(squares)

million = list(range(1, 1_000_001))
# for number in million:
#     ##print(number)
# ##print(min(million))
# ##print(max(million))
# ##print(sum(million))

# for number in range(3, 31, 3):
#     ##print(number)

# for number in range(1, 11):
#     cube_in_number = number**3
#     ##print(cube_in_number)

# cube = [values**3 for values in range (1, 11)]
# ##print(cube)


#TOPIC: Slicing a list
players = ['charlse', 'martina', 'michaella', 'florence', 'eli']
players.append('joshua')
# ##print(players)


#TOPIC: Copying a list
new_set_players = players[:]
new_set_players.append('Neri')
# ##print(new_set_players)

#TOPIC: 4.10
##print("The first three items of the list are: ")
##print(players[:3])

##print("The Middle items of the list are: ")
middle_item = (len(players) // 2) + -1
##print(players[middle_item])

##print("The last three items of the list are: ")
##print(players[-3:])


#TOPIC: 4.11
friend_pizzas = favorite_pizzas[:]
favorite_pizzas.append('Peppironi')
friend_pizzas.append('Meat balls')

#print("My favorite pizzas are: ")
#for pizza in favorite_pizzas:
    #print(pizza)

#print("My frind favorite pizzas are: ")
#for pizza in friend_pizzas:
    #print(pizza)

#TOPIC: Tuple immutable means cannot be change nut can be redefine the variable to change the value
# dimension = (250, 0)
# dimension[0] = 2
#print(dimension[0])


#TOPIC: 4.13
foods = ('Salad', 'adobo', 'sinigang', 'chapsuy', 'bicol express')
# for food in foods:
#     print(food)

# foods[1] = 'baboy'

# foods = ('ice cream', 'adobo', 'sinigang', 'tortang talong', 'bicol express')
# for food in foods:
#     print(food)

#TOPIC: IF/Else statements
# for player in players:
#     if player == "joshua":
#         print(player.upper())
#     else:
#         print(player.title())

#TOPIC: IN and NOT IN
my_age = 23
your_age = 15
display = my_age >= 20 or your_age >=20
check_pizza = 'Eli' not in players

#print(check_pizza)

#emppty list is considered as false
#list with values/items considered true

available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'adding {requested_topping}')
#     else:
#         print(f'sorry we dont have anymore {requested_topping}')

#TOPIC: 5.8 Hello admin
usernames = []

def is_empty_list(usernames):
    try:
        usernames[0]
    except IndexError:
        return True
    return None

for username in usernames:
    if is_empty_list(usernames) is not False:
        print('We need to find more users')
    elif username.lower() == 'admin':
        print(f'Hello {username}, would you like to see our report? ')
    else:
        print(f'Welcome back {username}')
