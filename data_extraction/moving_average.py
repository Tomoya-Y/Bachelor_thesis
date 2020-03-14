import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import copy
import japanize_matplotlib
import sys

input_name = sys.argv[1]

force = np.loadtxt(input_name+"/force.csv", delimiter=",")

move_steer_force = []
move_vel_force = []
N = 5
N_array = np.ones(N)/N
move_steer_force = np.convolve(force[:,1], N_array, mode='same')
move_vel_force = np.convolve(force[:,2], N_array, mode='same')

force[:,1] = move_steer_force
force[:,2] = move_vel_force

np.savetxt(input_name+"/moveforce.csv", force, delimiter=",")
