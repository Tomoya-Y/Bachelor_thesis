#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import pprint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import math
import copy
import japanize_matplotlib

filename = "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-06-17-23-10"

def route(filename):
    # odom_data = pd.read_csv(filename, usecols=[5, 6, 10, 11])
    odom_data = np.loadtxt(filename+"/odom.csv", delimiter=",")
    force_data = np.loadtxt(filename+"/moveforce.csv", delimiter=",")
    # odom_data = odom_data.values
    x = odom_data[:,0]
    y = odom_data[:,1]
    start = 0
    while y[start] == y[0]:
        start+=1
    print(start)
    zori = odom_data[start,2]
    wori = odom_data[start,3]
    # zori = np.mean(odom_data[:30, 2], axis=0)
    # wori = np.mean(odom_data[:30, 3], axis=0)
    theta = 2 * math.atan(zori/wori)
    rotation = np.array([[math.cos(-theta), -math.sin(-theta)], [math.sin(-theta), math.cos(-theta)]])
    x = x - x[start]
    y = y - y[start]
    before = np.array([x, y])
    after = np.zeros((before.shape[0], before.shape[1]))
    for i in range(before.shape[1]):
        after[:,i] = np.dot(rotation, before[:,i])
    new_x = after[0]
    new_y = after[1]
    force_index = []
    noforce_index = []
    force_x = []
    force_y = []
    noforce_x = []
    noforce_y = []

    # newforce_data = copy.copy(force_data)

    # for i in range(3, len(force_data)-5):
    #     if (abs(force_data[i-3,1]) <= 0.1) and (abs(force_data[i-2,1]) <= 0.1 and (abs(force_data[i-1,1]) <= 0.1)):
    #         if abs(force_data[i,1] > 0.1):
    #             if (abs(force_data[i+1,1]) > 0.1) and (abs(force_data[i+2,1]) > 0.1) and (abs(force_data[i+3,1]) > 0.1) and (abs(force_data[i+4,1]) > 0.1):
    #                 for j in range(50):
    #                     if i+j < len(force_data):
    #                         newforce_data[i+j,1]=0
    #             else:
    #                 newforce_data[i,1]=0

    # for i in range(20, len(force_data)-30):
    #     former_force_data = force_data[i-20:i,1]
    #     latter_force_data = force_data[i:i+30,1]
    #     if (len(former_force_data[abs(former_force_data)<=0.1]) > 10) and (len(latter_force_data[abs(latter_force_data)>0.1])>15):
    #         if i+30 < len(force_data):
    #             newforce_data[i:i+30,1]=0

    # for i in range(len(newforce_data)):
    #     if abs(newforce_data[i,1]) > 0.1:
    #         force_x.append(new_x[i])
    #         force_y.append(new_y[i])
    #         force_index.append(i)
    #     else:
    #         noforce_x.append(new_x[i])
    #         noforce_y.append(new_y[i])
    #         noforce_index.append(i)

    for i in range(start, len(force_data)):
        if abs(force_data[i,1]) > 0.1:
            force_x.append(new_x[i])
            force_y.append(new_y[i])
            force_index.append(i)
        else:
            noforce_x.append(new_x[i])
            noforce_y.append(new_y[i])
            noforce_index.append(i)

    # part_force_data = force_data[30:500,1]
    # print(len(part_force_data[abs(part_force_data)>0.1]))
    return new_x, new_y, force_x, force_y, noforce_x, noforce_y



new_x, new_y, force_x, force_y, noforce_x, noforce_y = route(filename)



plt.scatter(force_x, force_y, color="darkorange", s=15, label="介入あり")
plt.scatter(noforce_x, noforce_y, color="cornflowerblue", s=15, label="介入なし")

plt.xlabel("X [m]", fontsize=14)
plt.ylabel("Y [m]", fontsize=14)
plt.xlim(-0.5, 8)
plt.ylim(-0.5,10)

# triangle=patches.Rectangle(xy=(1.88, -0.53),width=0.24,height=0.38,ec="#000000",fc='k')
# plt.gca().add_patch(triangle)
#().set_aspect('equal', 'datalim')
# plt.xlim(-0.2, 4.5)
# plt.ylim(-1.14, 1.14)
plt.axes().set_aspect('equal')
plt.legend(fontsize=14)
plt.show()
