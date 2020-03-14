import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import matplotlib

filename1 = "/media/tomoya/Tomoya's_T5/outside_data/03-02-14-58-59"

filename2 = "/media/tomoya/Tomoya's_T5/outside_data/03-02-14-07-17"


twist1 = np.loadtxt(filename1+"/twist.csv", delimiter=",")
twist2 = np.loadtxt(filename2+"/twist.csv", delimiter=",")
vel1 = twist1[896:1696,2]
vel1_= twist1[9103:9977,2]
vel2 = twist2[10478:11294,2]

ndt1 = np.loadtxt(filename1+"/ndt.csv", delimiter=",")
ndt2 = np.loadtxt(filename2+"/ndt.csv", delimiter=",")
x1 = ndt1[896:1696, 1]
x1_= ndt1[9103:9977,1]
x2 = ndt2[10478:11294, 1]


plt.plot(x1, vel1, color="tab:orange")
plt.plot(x1_, vel1_, color="tab:orange", linestyle="dashed")
plt.plot(x2, vel2, color="tab:blue")
plt.xlabel("x [m]", fontsize=14)
plt.ylabel("Velocity [m/s]", fontsize=14)
# matplotlib.rcParams['pdf.fonttype'] = 42
# matplotlib.rcParams['ps.fonttype'] = 42
plt.legend()

plt.show()
