import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import copy
import japanize_matplotlib

filename = "/media/tomoya/Tomoya's_T5/202002data/outputlog_2020-02-03-16-56-03"

steer = np.loadtxt(filename+"/twist.csv", delimiter=",")
force = np.loadtxt(filename+"/force.csv", delimiter=",")
vel = 0.3
distance = (force[:, 0] - force[0, 0]) * vel

force_index = []
noforce_index = []
for i in range(len(force)):
    if abs(force[i,1]) > 0.1:
        force_index.append(i)
    else:
        noforce_index.append(i)

plt.scatter(distance[force_index], steer[force_index], s=1, label="介入あり")
plt.scatter(distance[noforce_index], steer[noforce_index], s=1, label="介入なし")
plt.ylim(-0.3, 0.3)
plt.xlabel("移動距離[m]", fontsize=14)
plt.ylabel("角速度[rad/s]", fontsize=14)
plt.legend()
plt.show()
