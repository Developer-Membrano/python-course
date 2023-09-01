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

