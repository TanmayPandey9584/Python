import matplotlib.pyplot as plt
import numpy as np



'''x=np.array([1,2,3,4,5,6])
y=np.array([1,2,3,4,5,6])
plt.title("Demo")
plt.xlabel("X")
plt.ylabel("Y")
'''

#You can use the keyword argument marker to emphasize each point with a specified marker:
'''
plt.plot(x,y,marker='_')
'''

#You can also use the shortcut string notation parameter to specify the marker.This parameter is also called fmt, and is written with this syntax:
#marker|line|color

'''
plt.plot(x,y,'o:r')
'''

#You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
'''
plt.plot(x,y,marker='o',ms=15)
'''

#You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
'''
plt.plot(x,y,marker='^',ms=15,mec='pink')
'''

#You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
'''
plt.plot(x,y,marker='*',ms=25,mec='black',mfc='red')
'''

#You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
'''
plt.plot(x,y,marker='*',ms=25,mec='red',mfc='orange',linestyle='dotted')
'''

#ou can use the keyword argument color or the shorter c to set the color of the line:
'''
plt.plot(x,y,marker='o',ms=25,mec='red',mfc='red',linestyle='-.',c='r')
'''

#You can use the keyword argument linewidth or the shorter lw to change the width of the line.
'''
plt.plot(x,y,marker='o',ms=25,mec='red',mfc='red',ls='-',c='black',lw=25)
'''

#You can plot as many lines as you like by simply adding more plt.plot() functions:
'''
x=np.array([5,6,2,3,4])
y=np.array([1,2,4,9,7])
plt.plot(x)
plt.plot(y)
'''

#Draw two lines by specifiyng the x- and y-point values for both lines:
'''
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)
'''

#With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
'''
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
'''

#With Pyplot, you can use the title() function to set a title for the plot.
'''
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
'''

#You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.
'''
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1={'family':"serif ",'color':"red",'size':20}
font2={'family':"serif ",'color':"black",'size':25}

plt.title("Demo",fontdict=font1)
plt.xlabel("Xlabel",fontdict=font2)
plt.ylabel("Ylable",fontdict=font2)

plt.plot(x,y)
'''

#You can use the loc parameter in title() to position the title.
'''
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title('Demo',loc='right')
plt.xlabel('Xlabel')
plt.ylabel('Ylabel')

plt.plot(x,y)
'''

#With Pyplot, you can use the grid() function to add grid lines to the plot.
'''
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()
'''

#You can use the axis parameter in the grid() function to specify which grid lines to display.
#You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).
'''
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x,y)
plt.grid(axis='y',c='red',ls='dotted',lw='25')
'''

#
import numpy as np

# Sample data
data = np.array([[1, 5, 8],
                 [2, 3, 10],
                 [4, 7, 9]])

# ptp along axis 0 (columns)
ptp_axis_0 = np.ptp(data, axis=0)
print("ptp (axis=0):", ptp_axis_0)  # Output: [3 4 2]
print(f'ptp no axis {np.ptp(data)}')
# ptp along axis 1 (rows)
ptp_axis_1 = np.ptp(data, axis=1)
print("ptp (axis=1):", ptp_axis_1)  # Output: [4 7 5]

plt.show()
