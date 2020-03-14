import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import copy
import japanize_matplotlib

filenames = ["/home/tomoya/0226vel1.csv",
"/home/tomoya/0226velstop.csv"
]

vel1 = np.loadtxt("/home/tomoya/0226vel1.csv", delimiter=",", usecols=1, skiprows=1)
plt.plot(vel1, label="Moving pedestrian")

vel2 = np.loadtxt("/home/tomoya/0226velstop.csv", delimiter=",", usecols=1, skiprows=1)
plt.plot(vel2, label="Stopping pedestrian")

# plt.ylim(0, 0.3)
plt.xlabel("Frame", fontsize=14)
plt.ylabel("Velocity of the vehicle [m/s]", fontsize=14)
plt.legend(fontsize=14)
plt.tick_params(labelsize=14)
plt.show()
