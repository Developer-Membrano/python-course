

def make_sandwiches(bread='Plain', *toppings):
    print(f"I'll be cooking a {bread} sandwich with these ff. toppings")
    for topping in toppings:
        print(topping)

make_sandwiches('Wheat bread', 'Ham', 'Macaroni', 'Hot sauce', 'cheeze', 'Mayonaise')



print("----------------------")


def user_profile(first_name, last_name, **userInfo):
    userInfo['first_name'] = first_name
    userInfo['last_name'] = last_name

    for key_info, value_info in userInfo.items():
        print(f'{key_info} : {value_info}')

user_profile('Kenny', 'Membrano', 
             current_situation='Successful Man', 
             status='Rich', 
             personality='Kind', 
             looks='Beautiful Man')
