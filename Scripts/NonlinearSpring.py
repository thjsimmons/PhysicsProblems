#======================================================================
# Github: https://github.com/thjsimmons
#======================================================================

# Solution to problem: https://brilliant.org/problems/nonlinear-resonance/

import numpy as np
from scipy.integrate import odeint
from numpy import sin, cos, pi, array
import matplotlib.pyplot as plt

# Plot max value in solution over different values of wext 

init = array([0, 0])
time = np.linspace(0.0, 1000, 1000*10)
wexts = np.linspace(0.0, 5, 500)
amps = np.zeros(wexts.shape[0])

# Get max amplitude of x(t) for each external force frequency: 
for i in range(wexts.shape[0]):
    print "i = ", i
    def deriv(z, t): # function to integrate 
        x,dxdt = z # initial conditions 
        dx2dt2 = -(2*x + 0.01*x**3) - 0.05*dxdt + np.sin(wexts[i] * t) # x equation of motion
        return np.array([dxdt, dx2dt2])

    sol = odeint(deriv, init, time) 
    amps[i] = np.max(np.abs(sol[:, 0])) # get max amplitude 

wres = wexts[np.argmax(amps)] # Get resonant frequency 
print "Resonant frequency = ", wres, " rad/s"

fig = plt.figure()
plt.title("Max Amplitude vs. Frequency (rad/s)")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Max Amplitude of x(t)")

plt.xlim([0, 5])
plt.ylim([0, 20])
plt.plot(wexts, amps, label='hi')
fig.savefig("NonlinearSpring.jpg")
plt.show() 

