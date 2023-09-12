import matplotlib.pyplot as plt
plt.style.available
plt.style.use('seaborn')

x_squares = [1, 4, 9, 16, 25]
y_squares = [5, 2, 3, 1, 7]


animals = {
    'id_birds' : [20, 30, 50, 33, 24],
    'population' : [100, 150, 300, 203, 53]
}

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot('id_birds', 'population', 'go-.', data=animals)  # Plot some data on the axes.

ax.set_title('Birds population by ID')
ax.set_xlabel("Population")
ax.set_ylabel("ID")
ax.tick_params(labelsize=8)

plt.show()