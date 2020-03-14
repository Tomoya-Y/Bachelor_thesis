import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as ticker
import matplotlib
import copy
# import japanize_matplotlib

filename = "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-06-17-23-10"

steer = np.loadtxt(filename+"/twist.csv", delimiter=",", usecols=1)
for i in range(len(steer)):
    if abs(steer[i])>0.5:
        steer[i]=steer[i+2]

force = np.loadtxt(filename+"/moveforce.csv", delimiter=",")
vel = 0.3
distance = (force[:, 0] - force[0, 0]) * vel

force_index = []
noforce_index = []
for i in range(len(force)):
    if abs(force[i,1]) > 0.1:
        force_index.append(i)
    else:
        noforce_index.append(i)

# plt.scatter(distance[force_index], steer[force_index], s=1, label="介入あり")
# plt.scatter(distance[noforce_index], steer[noforce_index], s=1, label="介入なし")
# plt.ylim(-0.3, 0.3)
# plt.xlabel("移動距離[m]", fontsize=14)
# plt.ylabel("角速度[rad/s]", fontsize=14)
# plt.legend()
# plt.show()

fig, ax1 = plt.subplots()

color1 = 'tab:blue'
ax1.set_ylabel('Torque applied to the handle [N $\cdot$ m]', fontsize=14)
ax1.plot(distance, force*2.5, color=color1, label="Torque")
r1 = patches.Rectangle(xy=(1.7, -1.5), width=1.1, height=3, fc="peachpuff")
r2 = patches.Rectangle(xy=(8.8, -1.5), width=1.6, height=3, fc="peachpuff")
plt.gca().add_patch(r1)
plt.gca().add_patch(r2)
# ax1.axhline(0.25, ls = "-.", color = "k")
# ax1.axhline(-0.25, ls = "-.", color = "k")
ax1.set_ylim(-1.5, 1.5)
ax1.tick_params(axis='y', labelsize=14)

ax2 = ax1.twinx()

color2 = 'tab:orange'
ax2.set_ylabel("Angle velocity of steering [rad/s]", fontsize=14)
# ax1.scatter(distance[force_index], steer[force_index], s=15, label="角速度(介入あり)")
# ax1.scatter(distance[noforce_index], steer[noforce_index], s=15, label="角速度(介入なし)")
ax2.plot(distance, steer, label="Angle velocity", color=color2)
ax2.set_ylim(-0.35,0.35)
ax2.tick_params(axis='y', labelsize=14)



color = 'tab:purple'
ax1.set_xlabel('Transit distance [m]', fontsize=14)
ax1.tick_params(axis='x', labelsize=14)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

# fig.legend(fontsize=14)
ax1.legend(loc = 'upper left', fontsize=14)
ax2.legend(loc = 'best', fontsize=14)
fig.tight_layout()

# matplotlib.rcParams['text.usetex'] = True
# matplotlib.rcParams['text.latex.preamble']="\\usepackage{sfmath}"

plt.show()
