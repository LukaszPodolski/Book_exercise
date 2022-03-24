import matplotlib.pyplot as plt

x_values = [10,8,8,6,7,5,6]
y_values  = [1,4,5,8,9,4,6]
fig, ax = plt.subplots()
ax.plot(x_values)
ax.scatter(x_values,y_values, s=11)
plt.show()