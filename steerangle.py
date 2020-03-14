import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import copy


filename = "/media/tomoya/Tomoya's_T5/0124"

# learnsteer  = np.loadtxt("/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-28-17-11-28/twist.csv", delimiter=",")
steer = np.loadtxt(filename+"/tomoyakun2.csv", delimiter=",", usecols=[0,6], skiprows=1)
pre_steer = np.loadtxt(filename+"/tomoyakun1.csv", delimiter=",", usecols=[0,6], skiprows=1)
image = np.loadtxt(filename+"/image_pub.csv", delimiter=",", usecols=[0,1], skiprows=1)
# steer = np.loadtxt("/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-28-17-11-28/twist.csv", delimiter=",")
# force_file = np.loadtxt(filename+"/force.csv", delimiter=",", usecols=1)
# realsteer = np.loadtxt(filename+"/twist.csv", delimiter=",")

# force_index = []
# noforce_index = []
# newforce_file = copy.copy(force_file)
# for i in range(20, len(force_file)-20):
#     former_force_file = force_file[i-20:i]
#     latter_force_file = force_file[i:i+20]
#     if (len(former_force_file[abs(former_force_file)<=0.1]) > 10) and (len(latter_force_file[abs(latter_force_file)>0.1])>10):
#         if i+30 < len(force_file):
#             newforce_file[i:i+30]=0
# for i in range(len(force_file)):
#     if abs(newforce_file[i]) > 0.1:
#         force_index.append(i)
#     else:
#         noforce_index.append(i)
# newforce_file = np.array(newforce_file)
# np.savetxt("/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-28-17-19-53/newforce.csv", newforce_file, delimiter=",")
# # for i in range(len(force_file)):
# #     if abs(force_file[i]) > 0.1:
# #         force_index.append(i)
# #     else:
# #         noforce_index.append(i)
#
# plt.scatter(force_index, steer[force_index], s=1)
# plt.scatter(noforce_index, steer[noforce_index], s=1)

plt.scatter(steer[:,0], steer[:,1], s=1, label="/ypspur_ros/cmd_vel")
plt.scatter(pre_steer[:,0], pre_steer[:,1], s=1, label="/predict_twist")
plt.scatter(image[:,0], image[:,1], s=0.1)
# plt.plot(steer[:,1])
# plt.plot(pre_steer[:,1])
# plt.plot(image)
plt.xlabel("ros_time")
plt.ylabel("steering_value")
# plt.plot(realsteer)

# plt.plot([0, 1000],[0.0, 0.0], "red", linestyle='dashed') # normal way
# plt.xlim(0, 1000)
plt.ylim(-0.3, 0.3)


# c = 0
# vel = 0.3
# # color_list = ["b", "b", "g", "y", "r", "r"]
# label = ["1st-1", "1st-2", "2nd-1", "2nd-2", "3rd-1", "3rd-2"]
# # label = ["1st-1", "1st-2", "2nd-1", "3rd-1", "3rd-2"]
# for filename in filenames4to6:
#     data = np.loadtxt(filename, delimiter=",")
#     distance = (data[:, 0] - data[0, 0]) * vel
#     # force = data[:, 1] * 2.5 #torque
#     force = data[:, 1] #raw_data
#     plt.plot(distance, force, label=label[c])
#     c += 1
#
# plt.ylim(-0.35, 0.35)
# plt.xlabel("distance [m]")
# plt.ylabel("torque [N・m]")
plt.legend()
plt.show()
