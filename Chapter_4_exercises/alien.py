alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}

if alien_0 == 'slow':
    x_increment = + 1
elif alien_0 == 'medium':
    x_increment = + 2
else:
    x_increment = + 3

alien_0['x_position'] = x_increment + alien_0['x_position']
print(f'the new position of the alien is: {alien_0["x_position"]}')