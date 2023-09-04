"""


dogs = [
    {
        'German Shepperd' : 'Joey De leon',
        'color' : 'Brownish Black',
        'address': ['Taguig', '2554', 'Near Katipunan']
     },
     {
        'Askal' : 'Philippine Dog',
        'color' : 'Brown',
        'address': ['Mandaluyong', '1664', 'Near Landbank']
      },
      {
        'K9' : 'Military Dog',
        'color' : 'Pure black',
        'address': ['Manila', '1550', 'Near Airport']
      }
]

for dog in dogs:
   for keys, values in dog.items():
      if keys == 'K9':
         print(dog.get('address'))




keys = ('Dog', 'Cat', 'Bird')
value = ('German Sheppard', 'Pomeranian Cat', 'Eagle')

new_animal_form = dict(zip(keys, value))
print(new_animal_form)

"""


d1 = {"name": "Alice", "age": 25, "job": "SWE"}
d2 = {"job": "Senior SWE", "location": "US", "age" : 30}
d1 |= d2
print(d1)

d3 = {"name": "Alice", "age": 25, "job": "SWE"}
d4 = {"job": "Senior SWE", "location": "US", "age" : 30}
d3 | d4
print(d3)