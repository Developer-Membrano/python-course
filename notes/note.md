#### 11 Methods of Dictionaries

sample dictionary 

    user = {
        0 : 'Mario',
        1 : 'Luigi',
        2 : 'James'
    }
    

###### values()
print(user.values()) --> [Mario, Luigi, James]

###### keys()
print(user.keys()) --> [0, 1, 2]

###### pop()
user.pop() --> by default it will remove the last key-value pair in the dictionary
popped = user.pop() --> the last key-value pair that has been remove will be stored in a variable popped
popped = user.pop(2) --> the 2 argument specify the key of a dictionary that will be removed and it's value will be stored in popped variable

###### popitem()
this method takes no argument
user.popitem() --> it returns/remove the last key-value pair of the dictionary

###### copy()
copy_dictionary = user.copy() --> it will create a copy of a dictionary from user{} any changes that will be made in copy_dictionary will not affect the user{} but if you made changes in user{} dictionary it will also affect the copy_dictionary

###### get()
user.get(key, 'default value of key is not exist')
user.get(1) --> Luigi
user.get(4, "Sorry key does not exist") --> it will print the default value which is "Sorry key does not exist" because the key 4 is does not exist in user{} dictionary

###### setdefault()
setdefault(key, default value) --> 
user.setdefault(0, "Mario the mario") the key 0 will have a default value of "Mario the mario" if it does not exist

###### clear()
user.clear() --> it will clear all the key-value pair of an dictionary and return an empty dictionary

###### fromkeys()
keys: An iterable specifying the keys of the new dictionary. This parameter is required.
value: The value for all keys. This parameter is optional. If it is not provided, the default value is None

keys = ('key1', 'key2', 'key3')
value = 0
my_dict = dict.fromkeys(keys, value)
print(my_dict) --> {'key1': 0, 'key2': 0, 'key3': 0}



###### items()
it is mostly use in for loop to access key-value pair

###### update()
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.update({'key2': 'new_value2', 'key3': 'value3'})
print(my_dict) --> {'key1': 'value1', 'key2': 'new_value2', 'key3': 'value3'}


###### instead of update() method we can use a better way to update a dictionary or merge using UNION OPERATOR
--> | 
d1 = {"name": "Alice", "age": 25, "job": "SWE"}
d2 = {"job": "Senior SWE", "location": "US"}
d3 = d1 | d2
print(d3) --> {'name': 'Alice', 'age': 25, 'job': 'Senior SWE', 'location': 'US'}

it will merge the two dictionary, pero kapag ang key ng d1 ay nag eexist sa d2 ang mangyayare ay magkakaroon ng update ng value sa key na nagkaroon ng duplication
at ang value na makukuha ay yung dictionary na nasa left side. 

--> |= --> in place 

d1 = {"name": "Alice", "age": 25, "job": "SWE"}
d2 = {"job": "Senior SWE", "location": "US", "age" : 30}
d1 |= d2
print(d1) --> ang value na makukuha ay yung dictionary na nasa righ  side.