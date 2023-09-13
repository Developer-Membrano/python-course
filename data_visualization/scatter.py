import matplotlib.pyplot as plt
plt.style.use('seaborn')

fig, axes = plt.subplots()
x_values = range(0, 100)
y_values = [x*2 for x in x_values]

axes.scatter(x_values, y_values, s=10)
axes.set_title('Square Number', fontsize=10)


plt.show()

