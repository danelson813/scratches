import matplotlib.pyplot as plt
import numpy as np

# x_values = [1,2,3,4,5,6,7,8,9,10]
# y_values = [203,200,191,160,140,105,85,72,66,50]
# plt.plot(x_values, y_values)


# plt.title('Remaining Money (USD) for 10 Days')
# plt.xlabel('Days')
# plt.ylabel('Money')
# plt.plot(x_values, y_values)

# plt.style.use('seaborn-v0_8-')
#
# y_values2 = [10,25,30,38,49,65,89,101,120,130]
# plt.plot(x_values, y_values2, color='#999999', linestyle="-", marker="*", label = 'Alice')
# plt.plot(x_values, y_values, color="red", marker="o", linestyle=":", label = 'Diana')
# plt.title('Remaining Money (USD) for 10 Days')
# plt.xlabel('Days')
# plt.ylabel('Money')
# plt.legend() #plt.legend(['Alice', 'Diana']) order is important


#
# plt.show()

# plt.style.use('grayscale') # Set the aesthetic style of the plots
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend();plt.show()

plt.show()
