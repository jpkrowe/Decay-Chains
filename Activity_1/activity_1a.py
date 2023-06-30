# Write a runge kutta method to solve the following differential equation
# dn_1/dt = -l*n_1
# dn_2/dt = l*n_1

import numpy as np
import matplotlib.pyplot as plt
import sys

# Command line arguments are used to take the initial values of n_1 and n_2 and the decay rate of n_1

# Function to calculate the value of dn_1/dt
def f1(n1, n2, l):
    return -l*n1

# Function to calculate the value of dn_2/dt
def f2(n1, n2, l):
    return l*n1

# Function to calculate the value of n_1 and n_2 using Runge-Kutta method
def rungeKutta(n1, n2, l, h, t):
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

n1 = np.zeros(10000)
n2 = np.zeros(10000)
# use command line arguments to take initial values of n_1 and n_2



n1[0] = sys.argv[1]
n2[0] = sys.argv[2]
l = sys.argv[3] # Decay rate for n_1
time_steps = sys.argv[4:] # Number of time steps

h = 0.01
t = np.linspace(0, 100, 10000)
for i in range(1, 10000):
    n1[i], n2[i] = rungeKutta(n1[i-1], n2[i-1], l, h, t[i])


# plot the values of n_1 and n_2
plt.plot(t, n1, label = 'n_1')
plt.plot(t, n2, label = 'n_2')
plt.xlabel('t')
plt.ylabel('n')
plt.legend()
plt.show()
