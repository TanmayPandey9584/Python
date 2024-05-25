import numpy as np
import matplotlib.pyplot as plt

x_train=np.array([1.0,3.0,4.0,6.0,8.0])
y_train=np.array([200.0,400.0,600.0,800.0,900.])

print(f"x_train {x_train}")
print(f"y_train {y_train}")

w=500
b=300
print(f"w: {w} and b: {b}")

def model(x,w,b):
    m=x.shape[0]
    f_wb=np.zeros(m)
    for i in range(m):
        f_wb[i]=w*x[i]+b

    return f_wb

temp=model(x_train,w,b)
plt.plot(x_train,temp,c="b",label="first prediction")
plt.scatter(x_train,y_train,marker="x",c="r",label="actual values")
plt.title("Housing Price")
plt.ylabel("Price")
plt.xlabel("Size")
plt.legend()
plt.show()
