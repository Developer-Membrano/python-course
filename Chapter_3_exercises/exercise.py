
names = ['Bernadette', 'Kenny', 'fluffy'] #TOPIC: excercise 3.1

#TOPIC: excercise 3.2
# print(f'Good day! {names[0]}')
# print(f'Have a nice day! {names[1]}')
# print(f'Cuteness overload {names[2]}')

# print('-----------------------------------------')
#TOPIC: excercise 3.3
motorcycle = ['Honda', 'Suzuki', 'Yamaha', 'Gold wing']
# print(f'Motorcycle {motorcycle[0]} is the cheapest one')
# print(f'Some people prefer {motorcycle[1]} because of engine')
# print(f'Some say\'s that {motorcycle[2]} is the best')
# print(f'Motorcycle {motorcycle[3]} is the expensive one')

# print('-------------------------------------')


#TOPIC: Adding and Modifying Elements in a list
motorcycle[2] = 'Mio' #inserting element in a given position(index)
motorcycle.append('Cruiser') #appending element in at the end of a list
motorcycle.insert(3, 'Ducati')  #inserting element in any given position by using index in a list


#TOPIC: Removing Elements in a list
#del motorcycle[1] -> #deleting an element in any given position by using index in a list
#popped_motocycle = motorcycle.pop() -> #removing the last element in a list
#popped_motocycle = motorcycle.pop(0) -> #removing an element in a list with given index
#motorcycle.remove('Honda') -> #removing an element in a list with given value

#TOPIC: exercise 3.4
guest_list = ['berna', 'kenny', 'fluffly']

# print(f'You\'re invited to dinner {guest_list[0]}')
# print(f'You\'re invited to dinner {guest_list[1]}')
# print(f'You\'re invited to dinner {guest_list[2]}')

#TOPIC: exercise 3.5
# popped_guest = guest_list.pop()
# print(f'{popped_guest} Can\'t make it to dinner ')
# new_guest = guest_list.append('dog')
# print(guest_list)

#TOPIC: exercise 3.6
#print("I have found a bigger dinner table we should invite three more guest")
guest_list.insert(0, "bird")
guest_list.insert(3, "cat")
guest_list.append("eagle")
# print(guest_list)


#TOPIC: exercise 3.7
#print('sorry I can only invite two people for dinner table')
popped_guest1 = guest_list.pop()
popped_guest2 = guest_list.pop()
popped_guest3 = guest_list.pop()
popped_guest4 = guest_list.pop()
# print(f'Im sorry {popped_guest1} you\'re not invited anymore')
# print(f'Im sorry {popped_guest2} you\'re not invited anymore')
# print(f'Im sorry {popped_guest3} you\'re not invited anymore')
# print(f'Im sorry {popped_guest4} you\'re not invited anymore')
# print('--------------------------------------------')
# print(f'You\'re still invited for the dinner {guest_list[0]}')
# print(f'You\'re still invited for the dinner {guest_list[1]}')

#TOPIC: exercise 3.8
del guest_list[0]
del guest_list[0]
# print(guest_list)


#TOPIC: Organizing list
cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort() #organize the list alphabetically
# cars.sort(reverse=True) #organize the list reverse-alphabetical order
# print(cars)
# print(sorted(cars)) #organize the list alphabetically temporarily
# print(cars)
cars.reverse()
total_cars = len(cars)
# print(cars)
# print(total_cars)

#TOPIC: Exercise 3.8
locations = ['New Zeland', 'Japan', 'Palawan', 'Canada', 'Paris']
#print(locations)
#print(sorted(locations))
#print(locations)
#print(sorted(locations, reverse=True))
#print(locations)
locations.reverse()
locations.reverse()
locations.sort()
locations.sort(reverse=True)
#print(locations)

total_guest = len(guest_list)
print(total_guest)