import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches

# filenames = [
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-09-31",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-10-49",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-12-05",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-13-00",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-15-25",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-16-06",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-17-08",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-18-19",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-19-34",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-20-32"
# ]

filename = "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-03-05-11-20-25"

# file1 = np.loadtxt("/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-24-19-09-31"+"/ndt.csv", delimiter=",")
# ndt = np.loadtxt(filename+"/ndt.csv", delimiter=",")
# x_base = ndt[4,1]
# y_base = ndt[4,2]
# print(x_base)
# print(y_base)
# z = ndt[4,3]
# w = ndt[4,4]
# theta = 2 * math.atan(z/w)
# print(theta)
# rotation = np.array([[math.cos(-theta), -math.sin(-theta)], [math.sin(-theta), math.cos(-theta)]])
# xy_list = []
# c = 0
# color_list = ["b", "b", "b", "g", "g", "g", "r", "r", "r"]

ndt = np.loadtxt(filename+"/ndt.csv", delimiter=",")
x = ndt[:, 1]
y = ndt[:, 2]
print(x[0])
print(y[0])
# x = x - x[0]
# y = y - y[0]
x = -x
y = -y
# before = np.array([x, y])
# after = np.zeros((before.shape[0], before.shape[1]))
# for i in range(before.shape[1]):
#     after[:,i] = np.dot(rotation, before[:,i])
# new_x = after[0]
# new_y = after[1]

force = np.loadtxt(filename+"/force.csv", delimiter=",")
steer_force = force[:,1]
vel_force = force[:,2]

steerforce_index = []
steernoforce_index = []
velforce_index = []
velnoforce_index = []
noforce_index = []
bothforce_index = []
for i in range(len(steer_force)):
    if (abs(steer_force[i]) > 0.1) and (abs(vel_force[i]) > 0.1):
        # plt.scatter(x[i], y[i], color="tab:orange")
        bothforce_index.append(i)
    elif abs(steer_force[i] > 0.1):
        steerforce_index.append(i)
        # plt.scatter(x[i], y[i], color="tab:red", s=5)
    elif abs(vel_force[i] > 0.1):
        velforce_index.append(i)
        # plt.scatter(x[i], y[i], color="tab:blue", s=5)
        # steernoforce_index.append(i)
        # velnoforce_index.append(i)
    else:
        # plt.scatter(x[i], y[i], color="k", s=5)
        noforce_index.append(i)

plt.scatter(x[noforce_index], y[noforce_index], color="lightgray", s=5)
plt.scatter(x[bothforce_index], y[bothforce_index], color="tab:orange", s=5, label="both")
plt.scatter(x[steerforce_index], y[steerforce_index], color="tab:red", s=5, label="steer")
plt.scatter(x[velforce_index], y[velforce_index], color="tab:green", s=5, label="vel")
plt.legend()

#     xy_list.append([new_x,new_y])
# plt.plot(x[160:], y[160:])
# fig = plt.figure()
# ax1 = fig.add_subplot(5, 2, 1)
# ax1.plot(xy_list[0][0],xy_list[0][1], color="red")
# ax2 = fig.add_subplot(5, 2, 2)
# ax2.plot(xy_list[1][0],xy_list[1][1], color="red")
# ax3 = fig.add_subplot(5, 2, 3)
# ax3.plot(xy_list[2][0],xy_list[2][1], color="red")
# ax4 = fig.add_subplot(5, 2, 4)
# ax4.plot(xy_list[3][0],xy_list[3][1], color="red")
# ax5 = fig.add_subplot(5, 2, 5)
# ax5.plot(xy_list[4][0],xy_list[4][1], color="red")
# ax6 = fig.add_subplot(5, 2, 6)
# ax6.plot(xy_list[5][0],xy_list[5][1], color="red")
# ax7 = fig.add_subplot(5, 2, 7)
# ax7.plot(xy_list[6][0],xy_list[6][1], color="red")
# ax8 = fig.add_subplot(5, 2, 8)
# ax8.plot(xy_list[7][0],xy_list[7][1], color="red")
# ax9 = fig.add_subplot(5, 2, 9)
# ax9.plot(xy_list[8][0],xy_list[8][1], color="red")
# ax10 = fig.add_subplot(5, 2, 10)
# ax10.plot(xy_list[9][0],xy_list[9][1], color="red")
#
# plt.xlim(-0.5, 12)
# plt.ylim(-1.165, 1.135)
plt.xlabel("x [m]")
plt.ylabel("y [m]")

# r = patches.Rectangle(xy=(2.345, -0.53), width=0.31, height=0.53, ec='k', fill=False)
# r = patches.Rectangle(xy=(2.345, 0), width=0.31, height=0.53, ec='k', fill=False)
# r = patches.Rectangle(xy=(3.845, -0.53), width=0.31, height=0.53, ec='k', fill=False)
# r = patches.Rectangle(xy=(3.845, 0), width=0.31, height=0.53, ec='k', fill=False)
# r = patches.Rectangle(xy=(5.345, -0.53), width=0.31, height=0.53, ec='k', fill=False)
# r = patches.Rectangle(xy=(5.345, 0), width=0.31, height=0.53, ec='k', fill=False)
# r = patches.Rectangle(xy=(6.845, -0.53), width=0.31, height=0.53, ec='k', fill=False)
# r = patches.Rectangle(xy=(6.845, 0), width=0.31, height=0.53, ec='k', fill=False)
# r = patches.Rectangle(xy=(8.345, -0.53), width=0.31, height=0.53, ec='k', fill=False)
# r = patches.Rectangle(xy=(8.345, 0), width=0.31, height=0.53, ec='k', fill=False)
# plt.gca().add_patch(r)
plt.gca().set_aspect('equal')
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble']="\\usepackage{sfmath}"
plt.savefig('figure10.eps', bbox_inches="tight", pad_inches=0.05)
plt.show()
