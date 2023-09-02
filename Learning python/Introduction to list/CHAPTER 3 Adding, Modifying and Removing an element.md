```python
motorcycle = ['Honda', 'Suzuki', 'Yamaha', 'Gold wing'] #list

#Adding and Modifying Elements in a list
motorcycle[2] = 'Mio' #inserting element in a given position(index)
motorcycle.append('Cruiser') #appending element in at the end of a list
motorcycle.insert(3, 'Ducati')  #inserting element in any given position by using index in a list

#Removing Elements in a list
del motorcycle[1] #deleting an element in any given position by using index in a list
popped_motocycle = motorcycle.pop() #removing the last element in a list
popped_motocycle = motorcycle.pop(0) #removing an element in a list with given index
motorcycle.remove('Honda') #removing an element in a list with given value
```

