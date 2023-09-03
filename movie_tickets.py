from collections import Counter

animals_welfare = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# while 'cat'.lower() in animals_welfare and 'dog'.lower() in animals_welfare:
#     animals_welfare.remove('cat')
#     animals_welfare.remove('dog')

# print(animals_welfare)


sandwich_orders = []
flag = ['done', 'exit', 'quit', 'no']


# while True:
#     list_of_sandwiches = str(input("Add a Sandwich to Menu: "))
#     if list_of_sandwiches in flag:
#         break

#     sandwich_orders.append(list_of_sandwiches)

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print("sorry we run out of pastrami! ")

# finished_sandwiches = sandwich_orders.copy()
# for sandwich in finished_sandwiches:
#     print(f'I made youre {sandwich} sandwich')


list_of_places = {}
name_prompt = "What is your Name: "
place_prompt = "Where would you like to go: "
quit_prompt = "Do you want to continue the poll?  "


while True:
    user_name = str(input(name_prompt))
    dream_place = str(input(place_prompt))

    #append the name as key and dream place as value to list_of_places object
    list_of_places[user_name] = dream_place.lower()

    #ask user if they want to continue the poll
    user_quit = str(input(quit_prompt))
    if user_quit.lower() in flag:
        break


#result of the poll
list_of_chosen_place = []
for user_name, user_dream_place in list_of_places.items():
    list_of_chosen_place.append(user_dream_place)

result_count = Counter(list_of_chosen_place)

for item, count in result_count.items():
    print(f"{item}: {count}")