import numpy as np
from scipy.integrate import odeint
from numpy import sin, cos, pi, array
import matplotlib.pyplot as plt

def path(theta):
    # return x, y
    # ends when x final
    a = 15
    b = 25
    u = 20
    m = 1
    f = 10
    g = 10

    ta = a /(u * cos(theta))
    tb = b /(u * cos(theta))

    ya = u*sin(theta)*ta - 0.5*g*ta**2
    ya_dot = u*sin(theta) - g*ta

    yb = ya + ya_dot*tb + 0.5*(f-g)*tb**2
    yb_dot = ya_dot + (f-g)*tb
    
    time = np.linspace(0.0, 10.0, 1000)
    
    x = np.zeros(time.shape[0])
    y = np.zeros(time.shape[0])
   
    for i in range(time.shape[0]):
        t = time[i]
        x_t = u * cos(theta) * t
        x[i] = x_t

        if x_t < a:
            y_t = u*sin(theta)*t - 0.5*g*t**2
            y[i] = y_t
        elif a < x_t < b:
            y_t = ya + ya_dot*(t-ta) + 0.5*(f-g)*(t-ta)**2
            y[i] = y_t
        else:
            y_t = yb + yb_dot*(t-tb-ta) - 0.5*g*(t-tb)**2
            y[i] = y_t
            if y_t < 0:
                y[i]  = 0
    return (x,y)


def x_resample(path):
    # Resample so that # of points is a function of the x range
    (x_init, y_init) = path
    x_range = np.max(x_init)
    x_new = np.linspace(0.0, 60, 1000)
    y_new = np.zeros(x_new.shape[0])

    count = 1

    y_new[0] = y_init[0]
    y_new[-1] = y_init[-1]
    
    for i in range(1000-1):
        slope = (y_init[i+1]-y_init[i])/(x_init[i+1]-x_init[i])
        if count == 1000:
            break
        while x_new[count]< x_init[i+1]:
            y_new[count] = y_init[i] + slope * (x_new[count]-x_init[i])
            count += 1
            if count == 1000:
                break
            
    return (x_new, y_new)
    
def boundary(angles):
   
    x_res = np.linspace(0.0, 60, 1000)
    xy_list = []
    u = 20
    curve = np.zeros(x_res.shape[0])

    for theta in angles:
        xy_list.append(x_resample(path(theta)))

    for i in range(x_res.shape[0]):
        
        maxy = -1
        mdex = -1
        for index in range(len(xy_list)):
            (x,y) = xy_list[index]
            if y[i] > maxy:
                maxy  = y[i]
                mdex = index
        curve[i] = maxy
    return (x_res, curve)
        
def integral(path): # riemann discrete integral
    (x,y) = path
    dx = x[1] - x[0]
    return dx * np.sum(y)

max_angle = 80/180 * np.pi # 80 / 180 * pi

angles = np.linspace(0.0, max_angle, 100)
plt.xlim([0, 100])
plt.ylim([0, 50])

for theta in angles:
    
    (x,y) = path(theta)
    #plt.plot(x, y, label='hi')
    
(x, curve) = boundary(angles)

print("integral = ", integral((x, curve)))
plt.plot(x, curve, 'k', label='hi')
plt.show()
