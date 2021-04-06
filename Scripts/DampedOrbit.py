
#======================================================================
# Github: https://github.com/thjsimmons
#======================================================================

# Solution to problem: https://brilliant.org/problems/damped-orbit/?ref_id=1613656

import numpy as np
from scipy.integrate import odeint
from numpy import sin, cos, pi, array
import matplotlib.pyplot as plt

def deriv(z, t): # function to integrate 

    x, y, dxdt, dydt = z # initial conditions 

    dx2dt2 = -10.0/(x**2 + y**2)**(1.5) * x - 0.1 * dxdt # x equation of motion
    dy2dt2 = -10.0/(x**2 + y**2)**(1.5) * y - 0.1 * dydt # y equation of motion

    return np.array([dxdt, dydt, dx2dt2, dy2dt2])

init = array([1.0, 0, 0, 10.0**0.5]) 
time = np.linspace(0.0, 10.0, 10000)
sol = odeint(deriv, init, time)

# Get Solution
for i in range(len(time)):
    (x, y, _, _)  = sol[i]
    radius = (x**2 + y**2)**0.5
  
    if abs(radius - 0.2) < 0.001: 
        print "Time = ", time[i], ", Radius = ", radius
        break

# Plot Solution
fig = plt.figure()
plt.title("Particle Path")
plt.xlabel("x coord")
plt.ylabel("y coord")
plt.xlim([-1, 1])
plt.ylim([-1, 1])
plt.plot(sol[:, 0], sol[:, 1], label='hi')
fig.savefig("DampedOrbit.jpg")
plt.show()

