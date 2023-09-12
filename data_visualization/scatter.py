import matplotlib.pyplot as plt
plt.style.use('seaborn')

fig, axes = plt.subplots()
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

axes.scatter(x_values, y_values, s=200)



axes.set_title('Square Number', fontsize=10)


plt.show()

