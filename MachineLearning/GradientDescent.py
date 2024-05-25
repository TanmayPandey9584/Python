import math, copy
import matplotlib.pyplot as plt
import numpy as np
from CostFunction import costfunction
from lab_utils_uni import plt_house_x, plt_contour_wgrad, plt_divergence, plt_gradients

# Load our data set
x_train = np.array([1.0, 2.0, 3.0, 4.0])   #features
y_train = np.array([300.0, 400.0, 500.0, 600.0])   #target value

def ComputeDescent(x, y, w, b):
    m=x.shape[0]
    dj_db=0
    dj_dw=0
    for i in range(m):
        f_wb=w*x[i]+b
        dj_dwi=(f_wb-y[i]) * x[i]
        dj_dbi=(f_wb-y[i])
        dj_dw= dj_dw + dj_dwi
        dj_db+=dj_dbi
    dj_db=dj_db/m
    dj_dw=dj_dw/m

    return dj_dw,dj_db

def GD(x,y,w_in,b_in,alpha,itters,cost_function,gradient_function):
    J_history=[]
    p_history=[]
    w=w_in
    b=b_in

    for i in range(itters):
        dj_dw,dj_db=gradient_function(x,y,w,b)
        b=b-alpha*dj_db
        w=w-alpha*dj_dw

        if i<10000:
            J_history.append(cost_function(x,y,w,b))
            p_history.append([w,b])

        if i% math.ceil(itters/10)==0:
            print(f"Iteration {i:4}: Cost {J_history[-1]:0.2e} ",
                  f"dj_dw: {dj_dw:0.3e}, dj_db: {dj_db:0.3e}  ",
                  f"w: {w:0.3e}, b:{b:0.5e}")

    return w,b,J_history,p_history
"""
w_innit=0
b_innit=0

itters=10000
curr_alpha=1.0e-2

w_final,b_final,Jhist,Phist=GD(x_train,y_train,w_innit,b_innit,curr_alpha,itters,costfunction,ComputeDescent)

print(f"(w,b) found by GD is ({w_final:0.4f},{b_final:0.4f})")

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, figsize=(12,4))
ax1.plot(Jhist[:100])
ax2.plot(1000 + np.arange(len(Jhist[1000:])), Jhist[1000:])
ax1.set_title("Cost vs. iteration(start)");  ax2.set_title("Cost vs. iteration (end)")
ax1.set_ylabel('Cost')            ;  ax2.set_ylabel('Cost')
ax1.set_xlabel('iteration step')  ;  ax2.set_xlabel('iteration step')
plt.show()

print(f"1000 sqft house prediction {w_final*1.0 + b_final:0.1f} Thousand dollars")
print(f"1200 sqft house prediction {w_final*1.2 + b_final:0.1f} Thousand dollars")
print(f"2000 sqft house prediction {w_final*2.0 + b_final:0.1f} Thousand dollars")
"""


w_innit=0
b_innit=0

itters=10
curr_alpha=8.0e-1

w_final,b_final,Jhist,Phist=GD(x_train,y_train,w_innit,b_innit,curr_alpha,itters,costfunction,ComputeDescent)



# Convert variables to higher precision data types
Phist = np.array(Phist, dtype=np.float16)
Jhist = np.array(Jhist, dtype=np.float16)
x_train = np.array(x_train, dtype=np.float16)
y_train = np.array(y_train, dtype=np.float16)


plt_divergence(Phist,Jhist,x_train,y_train)
plt.show()

