import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import japanize_matplotlib
import copy

# filename = "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-23-25"
#
# twist_data = np.loadtxt(filename+"/twist.csv", delimiter=",")
#
# vel1 = twist_data[:,2]
# vel1 = vel1[vel1 > 0]
# vel1 = vel1[vel1 < 0.5]
# # vel.remove
# vel2 = copy.copy(vel1)
# vel2 = np.insert(vel2, 0, 0)
# vel2 = vel2[:-1]
# accel = vel1 - vel2
# sum_accel = np.sum(accel[1:-1])
# print(sum_accel)

# filenames = [
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-21-33",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-21-49",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-22-05",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-22-18",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-22-40",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-22-55",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-23-12",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-23-25",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-23-49",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-24-01",
#
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-24-47",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-24-59",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-25-12",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-25-24",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-25-37",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-25-49",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-26-01",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-26-15",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-26-28",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-25-13-26-44"
# ]

filenames = [
"/media/tomoya/Tomoya's_T5/0224/0226test1.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test2.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test3.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test4.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test5.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test6.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test7.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test8.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test9.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test10.csv",

"/media/tomoya/Tomoya's_T5/0224/0226test11.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test12.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test13.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test14.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test15.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test16.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test17.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test18.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test19.csv",
"/media/tomoya/Tomoya's_T5/0224/0226test20.csv",
]

i=0
for filename in filenames:
    # twist_data = np.loadtxt(filename+"/twist.csv", delimiter=",")
    twist_data = np.loadtxt(filename, delimiter=",", skiprows=1)
    # vel3 = twist_data[:,2]
    vel3 = twist_data[:,1]
    vel3 = vel3[vel3 > 0]
    vel3 = vel3[vel3 < 0.5]
    # vel.remove
    vel4 = copy.copy(vel3)
    vel4 = np.insert(vel4, 0, 0)
    vel4 = vel4[:-1]
    accel2 = vel3 - vel4
    sum_accel = np.sum(accel2[1:-1])
    if i<10:
        # plt.plot(vel3[1:-1], color="tab:orange", label="加速")
        plt.plot(accel2[1:-1], color="tab:orange")
        # print("加速する(値がプラスになる)はずだった")
        print(sum_accel)
    elif i<20:
        # plt.plot(vel3[1:-1], color="tab:blue", label="減速")
        plt.plot(accel2[1:-1], color="tab:blue")
        # print("減速する(値がマイナスになる)はずだった")
        print(sum_accel)
    i+=1



# plt.ylim(-0.1, 0.6)
plt.xlabel("フレーム", fontsize=14)
plt.ylabel("速度", fontsize=14)
plt.legend()
plt.show()
