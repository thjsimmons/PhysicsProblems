import numpy as np
from scipy.integrate import odeint
from numpy import sin, cos, pi, array
import matplotlib.pyplot as plt


def deriv(z, t): # pass in initial conditions, time interval 

    x, y, dxdt, dydt = z # initial conditions 

    dx2dt2 = -10.0/(x**2 + y**2)**(3/2) * x - 0.1 * dxdt
    dy2dt2 = -10.0/(x**2 + y**2)**(3/2) * y - 0.1 * dydt

    return np.array([dxdt, dydt, dx2dt2, dy2dt2])


init = array([1, 0, 0, 10**0.5])
time = np.linspace(0.0, 10.0, 100000)
sol = odeint(deriv, init, time)

# Get solution:

for i in range(len(time)):
    #print(time[i])
    radius = (sol[i][0]**2 + sol[i][1]**2)**0.5
    if abs(radius - 0.2) < 0.00001:
        print("Time = ", time[i])
        print("Radius = ", radius)
    
    
    
plt.xlim([-1, 1])
plt.ylim([-1, 1])
plt.plot(sol[:, 0], sol[:, 1], label='hi')
plt.show()
