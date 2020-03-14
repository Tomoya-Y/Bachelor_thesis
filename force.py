import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import japanize_matplotlib


filename = "/media/tomoya/Tomoya's_T5/outside_data/03-02-14-07-17"

vel = 0.3
force_data = np.loadtxt(filename+"/moveforce.csv", delimiter=",")

distance = (force_data[:, 0] - force_data[0, 0]) * vel

# steer_force = force_data[:, 1] #raw_data
# steer_force_index = []
# nosteerforce_index = []
# for i in range(len(force_data)):
#     if abs(force_data[i,1]) > 0.1:
#         steer_force_index.append(i)
#     else:
#         nosteerforce_index.append(i)
# plt.plot(distance, steer_force*2.5)

# plt.scatter(distance[force_index], force_data[force_index,1]*2.5, s=15, label="介入あり")
# plt.scatter(distance[noforce_index], force_data[noforce_index,1]*2.5, s=15, label="介入なし")

vel_force = force_data[:, 2]
vel_force_index = []
novelforce_index = []
for i in range(len(force_data)):
    if abs(force_data[i,2]) > 0.1:
        vel_force_index.append(i)
    else:
        novelforce_index.append(i)

plt.plot(distance, vel_force*2.5)


plt.axhline(0.25, ls = "-.", color = "k")
plt.axhline(-0.25, ls = "-.", color = "k")
plt.ylim(-1.5, 1.5)
plt.xlabel("移動距離[m]", fontsize=14)
plt.ylabel("トルク[N・m]", fontsize=14)
plt.legend()
plt.show()
