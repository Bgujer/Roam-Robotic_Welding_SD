import numpy as np

# coordinates
x1 = 220.1  #mm
x2 = 630    #mm
y1 = 175.4  #mm
y2 = -186.6 #mm

del_x = x2 - x1
del_y = y2 - y1
del_xy = np.array([del_y, del_x, del_y, del_x])

# manual input
#depression = np.array([ xxx.x, xxx.x, xxx.x, xxx.x]) 

# user input
depression = [0,0,0,0]
for i, x in enumerate(depression):
    depression[i] = float(input("Enter dial indicator value: "))
    print("Input recieved")

depression = np.array(depression)
dep_mm = np.array(depression / 1000 * 25.4)

del_dep = [0,0,0,0]
for i, x in enumerate(dep_mm):
    del_dep[i] = dep_mm[i] - dep_mm[i-1]

del_dep = np.array(del_dep)

# x angle
a_x = np.arctan(np.divide(del_dep[1], del_xy[1]))
a_x_deg = a_x *180 / np.pi

# y angle
a_y = np.arctan(np.divide(del_dep[2], del_xy[2]))
a_y_deg = -a_y *180 / np.pi

print(f"Angle offset in degrees (x,y) = ",a_x_deg, a_y_deg)
