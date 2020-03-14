import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches

filename1 = "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-03-02-14-58"

filename2 = "/media/tomoya/Tomoya's_T5/outside_data/03-02-14-07-17"


ndt1 = np.loadtxt(filename1+"/ndt.csv", delimiter=",")
ndt2 = np.loadtxt(filename2+"/ndt.csv", delimiter=",")


x1 = ndt1[5060:5890, 1]
y1 = ndt1[5060:5890, 2]

x1_ = ndt1[13127:13902, 1]
y1_ = ndt1[13127:13902, 2]

x2 = ndt2[6559:7320, 1]
y2 = ndt2[6559:7320, 2]

plt.scatter(x1, y1, color="tab:orange", s=5)
plt.scatter(x1_, y1_, color="tab:orange", s=5)
plt.scatter(x2, y2, color="tab:blue", s=5)
plt.xlabel("x [m]", fontsize=14)
plt.ylabel("y [m]", fontsize=14)
plt.legend()

plt.gca().set_aspect('equal')
# plt.savefig('out_avoid.eps', bbox_inches="tight", pad_inches=0.05)
plt.savefig('out_avoid.png', bbox_inches="tight", pad_inches=0.05)
plt.show()
