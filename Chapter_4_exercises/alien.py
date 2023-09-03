alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'fast'}

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 50
else:
    x_increment = 0

print(f'Original position {alien_0["x_position"]}')
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'the new position of the alien is: {alien_0["x_position"]}')