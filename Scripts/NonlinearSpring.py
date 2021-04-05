import numpy as np
from scipy.integrate import odeint
from numpy import sin, cos, pi, array
import matplotlib.pyplot as plt


def deriv(z, t): # pass in initial conditions, time interval 

    x,dxdt = z # initial conditions 
    wext = 1.54
    dx2dt2 = -(2*x + 0.01*x**3) - 0.05*dxdt + np.sin(wext * t)

    return np.array([dxdt, dx2dt2])


init = array([0, 0])
time = np.linspace(0.0, 1000, 1000*10)
sol = odeint(deriv, init, time)

print(sol.shape)

plt.xlim([0, 1000])
plt.ylim([-20, 20])
plt.plot(time, sol[:, 0], label='hi')
plt.show()

