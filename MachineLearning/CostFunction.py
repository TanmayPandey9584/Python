import numpy as np
import matplotlib.pyplot as plt
from lab_utils_uni import soup_bowl

x_train=np.array([1.0,2.0,3.0,4.0])
y_train=np.array([200.0,300.0,400.0,500.0])

def costfunction(x,y,w,b):
    m=x.shape[0]
    cost_sum=0
    for i in range(m):
        f_wb=w*x[i]+b
    total_cost=1/(2*m) * cost_sum
    return total_cost

