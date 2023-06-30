# Write a runge kutta method to solve the following differential equation
# dn_1/dt = -l*n_1
# dn_2/dt = l*n_1

import numpy as np
import matplotlib.pyplot as plt
import sys 
from scipy.integrate import solve_ivp

# Command line arguments are used to take the initial values of n_1 and n_2 and the decay rate of n_1 and then a list of requested times

# Function to calculate the value of dn_1/dt
def f1(n1, n2, l):
    return -l*n1

# Function to calculate the value of dn_2/dt
def f2(n1, n2, l):
    return l*n1

def dy_dt(t, y):
    return np.array([f1(y[0], y[1], l), f2(y[0], y[1], l)])

# calculate the values of n_1 and n_2 over 10000 time steps


# use command line arguments to take initial values of n_1 and n_2
l = float(sys.argv[3]) # Decay rate for n_1
requested_times = np.array(sys.argv[4:], dtype=float) # Number of time steps
h = 0.01
t_span = (0, requested_times.max())
y0 = (float(sys.argv[1]), 0)
# Create a list of time steps from 0 to total_timesteps with a step size of h

sol = solve_ivp(dy_dt, t_span, y0, t_eval = np.linspace(0, requested_times.max(), 10000))
n1 = sol.y[0]
n2 = sol.y[1]
for k in requested_times:
    index = np.abs(sol.t - k).argmin()
    print("n_1 at t = ", k, " is ", n1[index])
    print("n_2 at t = ", k, " is ", n2[index])



# plot the values of n_1 and n_2
plt.plot(sol.t, n1, label = 'n_1')
plt.plot(sol.t, n2, label = 'n_2')
plt.xlabel('t')
plt.ylabel('n')
plt.legend()
plt.show()
