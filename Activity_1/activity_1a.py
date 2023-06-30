# Write a runge kutta method to solve the following differential equation
# dn_1/dt = -l*n_1
# dn_2/dt = l*n_1

import numpy as np
import matplotlib.pyplot as plt
import sys

# Command line arguments are used to take the initial values of n_1 and n_2 and the decay rate of n_1 and then a list of requested times

# Function to calculate the value of dn_1/dt
def f1(n1, n2, l):
    return -l*n1

# Function to calculate the value of dn_2/dt
def f2(n1, n2, l):
    return l*n1

# Function to calculate the value of n_1 and n_2 using Runge-Kutta method
def rungeKutta(n1, n2, l, h):
    k_1 = h*f1(n1, n2, l)
    l_1 = h*f2(n1, n2, l)
    k_2 = h*f1(n1 + 0.5*k_1, n2, l)
    l_2 = h*f2(n1, n2 + 0.5*l_1, l)
    k_3 = h*f1(n1 + 0.5*k_2, n2, l)
    l_3 = h*f2(n1, n2 + 0.5*l_2, l)
    k_4 = h*f1(n1 + k_3, n2, l)
    l_4 = h*f2(n1, n2 + l_3, l)
    n1 = n1 + (1.0/6.0)*(k_1 + 2*k_2 + 2*k_3 + k_4)
    n2 = n2 + (1.0/6.0)*(l_1 + 2*l_2 + 2*l_3 + l_4)
    return n1, n2

# calculate the values of n_1 and n_2 over 10000 time steps


# use command line arguments to take initial values of n_1 and n_2




l = float(sys.argv[3]) # Decay rate for n_1
requested_times = np.array(sys.argv[4:], dtype=float) # Number of time steps
h = 0.01
total_timesteps = requested_times.max()/h
n1 = np.array([sys.argv[1]], dtype=float)
n2 = np.array([sys.argv[2]], dtype=float)

# Create a list of time steps from 0 to total_timesteps with a step size of h
t = np.array([0], dtype=float)
for i in range(1, int(total_timesteps)):
    n1_temp, n2_temp = rungeKutta(n1[i-1], n2[i-1], l, h)
    n1 = np.append(n1, n1_temp)
    n2 = np.append(n2, n2_temp)
    t = np.append(t, t[-1]+h)
for k in requested_times:
    index = np.abs(t - k).argmin()
    print("n_1 at t = ", k, " is ", n1[index])
    print("n_2 at t = ", k, " is ", n2[index])



# plot the values of n_1 and n_2
plt.plot(t, n1, label = 'n_1')
plt.plot(t, n2, label = 'n_2')
plt.xlabel('t')
plt.ylabel('n')
plt.legend()
plt.show()
