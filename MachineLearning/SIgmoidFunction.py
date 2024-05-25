import matplotlib.pyplot as plt
import numpy as np


def sigmoid(z):
    g=1/np.exp(-z)
    return g

z=np.arange(-10,11)

y=sigmoid(z)
np.set_printoptions(precision=2)
print(z)
print(y)

plt.plot(z,y,c="blue",ls="-")
plt.xlabel("Y")
plt.ylabel("Z")
plt.title("Sigmoid Function")
plt.legend()
plt.show()