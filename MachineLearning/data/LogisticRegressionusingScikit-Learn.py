import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

X = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y = np.array([0, 0, 0, 1, 1, 1])

lrmodel=LogisticRegression()

lrmodel.fit(X,y)

ypred=lrmodel.predict(X)

print("Prediction on training set:", ypred)

print("Accuracy on training set:", lrmodel.score(X, y))

plt.plot(X,ypred,c="red",ls="-")
plt.show()


