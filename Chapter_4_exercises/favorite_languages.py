from random import choice

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

alien = {
    'first_name' : 'zombie',
    'last_name' : 'archneus',
    'age' : 'BC 200',
    'city' : 'Agharta'
}

glossary = {
    'string manipulation' : ['.lower()', '.upper()', '.title()'],
    'list' : ['slice list[:3]', 'stores information'],
    'tuple' : ['immutable', 'uses open parenthesis', 'items() to get key value pair'],
    'loop' : 'for loop',
    'conditional statement' : ['if', 'elif', 'else']
}

topic = 'string manipulation'
# print('I learn about ')
# for word in glossary:
#     if word.lower() == topic.lower():
#         print(glossary[topic])
#         # for words in glossary[topic]:
#         #     print(words)
#         result = ' , '.join(glossary[topic])
#         print(result)

aliens = []
power = [500, 600, 100, 200]
speed = ['slow', 'fast', 'medium']
color = ['green', 'yellow', 'black', 'red']

for alien in range(10):
    new_alien =  {'color': choice(color), 'power' : choice(power), 'speed' : choice(speed)}
    aliens.append(new_alien)
    if choice(color) == 'green':
        new_alien.update({'points' : 10})
    elif choice(color) == 'yellow':
        new_alien.update({'points' : 20})
    elif choice(color) == 'red':
        new_alien.update({'points' : 50})
    else:
        new_alien.update({'points' : 100})

#print(aliens)

google_users = {
    'Kenny05' : {
        'first_name' : 'Kenny',
        'last_name' : 'Membrano',
        'flag' : 'isActive'
    },
    'Berna21' : {
        'first_name' : 'Bern',
        'last_name' : 'Membrano',
        'flag' : 'somehowActive'
    }
}

current_user = 'Berna21'
for user_key, user_value in google_users.items():
    if user_key.lower() == current_user.lower():
        #print(user_value)
        print(f"Full Name: {user_value['first_name']} {user_value['last_name']}")
        print(f"Currently: {user_value['flag']}")

