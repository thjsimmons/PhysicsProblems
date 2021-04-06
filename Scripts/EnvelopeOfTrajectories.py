#======================================================================
# Github: https://github.com/thjsimmons
#======================================================================

# Solution to problem: https://brilliant.org/problems/envelope-of-trajectories-2/?ref_id=1614339

import numpy as np
from scipy.integrate import odeint
from numpy import sin, cos, pi, array
import matplotlib.pyplot as plt

    
a = 15.0 # x-position at which force starts
b = 25.0 # x-position at which force ends
u = 20.0 # initial velocity
m = 1.0  # particle mass 
f = 10.0 # force per unit mass on (a,b)
g = 10.0 # gravity 

# Get (x(t), y(t)) for each angle theta: 
def path(theta):
    ta = a /(u * cos(theta))                    # time @ x = a
    tb = b /(u * cos(theta))                    # time @ x = b
    ya = u*sin(theta)*ta - 0.5*g*ta**2          # y @ x = a  
    ya_dot = u*sin(theta) - g*ta                # y' @ x = a  
    yb = ya + ya_dot*tb + 0.5*(f-g)*tb**2       # y @ x = b 
    yb_dot = ya_dot + (f-g)*tb                  # y' @ x = b 
    
    time = np.linspace(0.0, 10.0, 1000)
    x = np.zeros(time.shape[0])
    y = np.zeros(time.shape[0])
   
    # Compute piece-wise path: 
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

# Resample (x(t), y(t)) -> (x, y(x))
def x_resample(path):

    (x_init, y_init) = path
    x_range = np.max(x_init)
    x_new = np.linspace(0.0, 60, 1000)
    y_new = np.zeros(x_new.shape[0])
    y_new[0] = y_init[0]
    y_new[-1] = y_init[-1]
    
    count = 1
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

# Get boundary curve B(x)
def boundary(angles):
   
    x_res = np.linspace(0.0, 60, 1000) # resulting x values 
    xy_list = [] # 
    curve = np.zeros(x_res.shape[0])

    for theta in angles:
        xy_list.append(x_resample(path(theta))) # (x, y(x)) for each angle

    for i in range(x_res.shape[0]):
        maxy = -1
        mdex = -1
        # get max y(x) @ each x for all angles:
        for index in range(len(xy_list)):
            (_,y) = xy_list[index]
            if y[i] > maxy:
                maxy  = y[i] 
                mdex = index
        curve[i] = maxy
    return (x_res, curve)
        
def integral(path): # Quadrature under B(x)
    (x,y) = path
    dx = x[1] - x[0]
    return dx * np.sum(y)

max_angle = 80.0/180.0 * np.pi # 80 / 180 * pi
angles = np.linspace(0.0, max_angle, 100.0)

fig = plt.figure()
plt.xlim(0, 60)
plt.ylim(0, 25)
plt.xlabel("x coord")
plt.ylabel("y coord")
plt.title("Projectile Trajectory Envelope")
for theta in angles:
    (x,y) = path(theta)
    plt.plot(x, y, label='hi')
    
(x, curve) = boundary(angles)
print "Integral Value = ", integral((x, curve))

plt.plot(x, curve, 'k', label='hi')
plt.savefig("EnvelopeOfTrajectories.jpg", dpi = 100)
plt.show()
