import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator


first_file = "/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-09-50-06/force.csv"
first_force = np.loadtxt(first_file, delimiter=",", usecols=1)

#from filenames1 to filenames3: learn from all data
filenames1 = ["/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-10-08-41/force.csv",
"/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-10-09-27/force.csv"
]

filenames2 = ["/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-10-47-41/force.csv",
"/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-10-49-47/force.csv"
]

filenames3 = ["/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-11-30-08/force.csv",
"/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-11-31-21/force.csv"
]

filenames4 = ["/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-12-08-48/force.csv",
"/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-12-09-36/force.csv"
]

# filenames5 = ["/media/tomoya/Tomoya's_T5/202001data/0111_5_2_1/force.csv"
# ]
#
# filenames6 = ["/media/tomoya/Tomoya's_T5/202001data/0111_6_2_1/force.csv"
# ]
#
# filenames7 = ["/media/tomoya/Tomoya's_T5/202001data/0111_7_2_1/force.csv"
# ]

all_file = []


#from filenames4 to filenames6: learn from intervention data
filenames8 = ["/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-10-08-41/force.csv",
"/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-10-09-27/force.csv"
]

filenames9 = ["/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-10-59-47/force.csv",
"/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-11-00-34/force.csv"
]

filenames10 = ["/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-11-38-18/force.csv",
"/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-11-39-13/force.csv"
]

filenames11 = ["/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-12-18-03/force.csv",
"/media/tomoya/Tomoya's_T5/202001data/outputlog_2020-01-27-12-18-52/force.csv"
]

# filenames12 = ["/media/tomoya/Tomoya's_T5/202001data/0111_5_2_2/force.csv"
# ]
#
# filenames13 = ["/media/tomoya/Tomoya's_T5/202001data/0111_6_2_2/force.csv"
# ]
#
# filenames14 = ["/media/tomoya/Tomoya's_T5/202001data/0111_7_2_2/force.csv"
# ]



force_array = []
len_array = []
force_inter_array = []
len_inter_array = []
percent_array = []
percent_inter_array = []

a = 0
b = 0
len_filename = 0
len_sum = len(first_force)
len_array.append(len_sum)
for filename in filenames1:
    data = np.loadtxt(filename, delimiter=",")
    force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
    rate = (len(data[abs(data[:,1]) > 0.1, 1])/len(data[:,1]))*100
    # print(len(data[abs(data) > 0.1]))
    # print("force1= ", force)
    # print("rate1= ", rate, "%")
    a = a + force
    b = b + rate
    len_filename = len_filename + len(data[:,1])
print(a)
len_sum = len_sum + len_filename
ave_a = a / len_filename
force_array.append(ave_a)
len_array.append(len_sum)
print("AVE_force1= ", a/len(filenames1))
print("AVE_rate1= ", b/len(filenames1), "%")
percent_array.append(b/len(filenames1))

a = 0
b = 0
len_filename = 0
for filename in filenames2:
    data = np.loadtxt(filename, delimiter=",")
    force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
    rate = (len(data[abs(data[:,1]) > 0.1, 1])/len(data[:,1]))*100
    # print(len(data[abs(data) > 0.1]))
    # print("force2= ", force)
    # print("rate2= ", rate, "%")
    a = a + force
    b = b + rate
    len_filename = len_filename + len(data[:,1])
print(a)
len_sum = len_sum + len_filename
ave_a = a / len_filename
force_array.append(ave_a)
len_array.append(len_sum)
print("AVE_force2= ", a/len(filenames2))
print("AVE_rate2= ", b/len(filenames2), "%")
percent_array.append(b/len(filenames2))

a = 0
b = 0
len_filename = 0
for filename in filenames3:
    data = np.loadtxt(filename, delimiter=",")
    force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
    rate = (len(data[abs(data[:,1]) > 0.1, 1])/len(data[:,1]))*100
    # print(len(data[abs(data) > 0.1]))
    # print("force3= ", force)
    # print("rate3= ", rate, "%")
    a = a + force
    b = b + rate
    len_filename = len_filename + len(data[:,1])
print(a)
len_sum = len_sum + len_filename
ave_a = a / len_filename
force_array.append(ave_a)
len_array.append(len_sum)
print("AVE_force3= ", a/len(filenames3))
print("AVE_rate3= ", b/len(filenames3), "%")
percent_array.append(b/len(filenames3))

a = 0
b = 0
len_filename = 0
for filename in filenames4:
    data = np.loadtxt(filename, delimiter=",")
    force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
    rate = (len(data[abs(data[:,1]) > 0.1, 1])/len(data[:,1]))*100
    # print(len(data[abs(data) > 0.1]))
    # print("force3= ", force)
    # print("rate3= ", rate, "%")
    a = a + force
    b = b + rate
    len_filename = len_filename + len(data[:,1])
print(a)
len_sum = len_sum + len_filename
ave_a = a / len_filename
force_array.append(ave_a)
len_array.append(len_sum)
print("AVE_force4= ", a/len(filenames4))
print("AVE_rate4= ", b/len(filenames4), "%")
percent_array.append(b/len(filenames4))

# a = 0
# b = 0
# len_filename = 0
# for filename in filenames5:
#     data = np.loadtxt(filename, delimiter=",")
#     force = sum(abs(data[abs(data[:, 1]) > 0.1, 1]))
#     rate = (len(data[abs(data[:, 1]) > 0.1, 1])/len(data[:, 1]))*100
#     # print(len(data[abs(data) > 0.1]))
#     # print("force3= ", force)
#     # print("rate3= ", rate, "%")
#     a = a + force
#     b = b + rate
#     len_filename = len_filename + len(data[:, 1])
# print(a)
# len_sum = len_sum + len_filename
# ave_a = a / len_filename
# force_array.append(ave_a)
# len_array.append(len_sum)
# print("AVE_force5= ", a/len(filenames5))
# print("AVE_rate5= ", b/len(filenames5), "%")
# percent_array.append(b/len(filenames5))
#
# a = 0
# b = 0
# len_filename = 0
# for filename in filenames6:
#     data = np.loadtxt(filename, delimiter=",")
#     force = sum(abs(data[abs(data[:, 1]) > 0.1, 1]))
#     rate = (len(data[abs(data[:, 1]) > 0.1, 1])/len(data[:, 1]))*100
#     # print(len(data[abs(data) > 0.1]))
#     # print("force3= ", force)
#     # print("rate3= ", rate, "%")
#     a = a + force
#     b = b + rate
#     len_filename = len_filename + len(data[:, 1])
# print(a)
# len_sum = len_sum + len_filename
# ave_a = a / len_filename
# force_array.append(ave_a)
# len_array.append(len_sum)
# print("AVE_force6= ", a/len(filenames6))
# print("AVE_rate6= ", b/len(filenames6), "%")
# percent_array.append(b/len(filenames6))
#
# a = 0
# b = 0
# len_filename = 0
# for filename in filenames7:
#     data = np.loadtxt(filename, delimiter=",")
#     force = sum(abs(data[abs(data[:, 1]) > 0.1, 1]))
#     rate = (len(data[abs(data[:, 1]) > 0.1, 1])/len(data[:, 1]))*100
#     # print(len(data[abs(data) > 0.1]))
#     # print("force3= ", force)
#     # print("rate3= ", rate, "%")
#     a = a + force
#     b = b + rate
#     len_filename = len_filename + len(data[:, 1])
# print(a)
# len_sum = len_sum + len_filename
# ave_a = a / len_filename
# force_array.append(ave_a)
# len_array.append(len_sum)
# print("AVE_force7= ", a/len(filenames7))
# print("AVE_rate7= ", b/len(filenames7), "%")
# percent_array.append(b/len(filenames7))

c = 0
d = 0
len_filename = 0
len_inter = 0
len_sum_inter = len(first_force)
len_inter_array.append(len_sum_inter)
for filename in filenames8:
    data = np.loadtxt(filename, delimiter=",")
    force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
    rate = (len(data[abs(data[:,1]) > 0.1, 1])/len(data[:,1]))*100
    c = c + force
    d = d + rate
    len_filename = len_filename + len(data[:,1])
    len_inter = len_inter + len(data[abs(data[:,1]) > 0.1, 1])
print(c)
len_sum_inter = len_sum_inter + len_inter
print(len_sum_inter)
ave_c = c / len_filename
force_inter_array.append(ave_c)
len_inter_array.append(len_sum_inter)
print("AVE_force8= ", c/len(filenames8))
print("AVE_rate8= ", d/len(filenames8), "%")
percent_inter_array.append(d/len(filenames8))

c = 0
d = 0
len_filename = 0
len_inter = 0
for filename in filenames9:
    data = np.loadtxt(filename, delimiter=",")
    force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
    rate = (len(data[abs(data[:,1]) > 0.1, 1])/len(data[:,1]))*100
    c = c + force
    d = d + rate
    len_filename = len_filename + len(data[:,1])
    len_inter = len_inter + len(data[abs(data[:,1]) > 0.1, 1])
print(c)
print(len_inter)
len_sum_inter = len_sum_inter + len_inter
print(len_sum_inter)
ave_c = c / len_filename
force_inter_array.append(ave_c)
len_inter_array.append(len_sum_inter)
print("AVE_force9= ", c/len(filenames9))
print("AVE_rate9= ", d/len(filenames9), "%")
percent_inter_array.append(d/len(filenames9))

c = 0
d = 0
len_filename = 0
len_inter = 0
for filename in filenames10:
    data = np.loadtxt(filename, delimiter=",")
    force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
    rate = (len(data[abs(data[:,1]) > 0.1, 1])/len(data[:,1]))*100
    c = c + force
    d = d + rate
    len_filename = len_filename + len(data[:,1])
    len_inter = len_inter + len(data[abs(data[:,1]) > 0.1, 1])
print(c)
len_sum_inter = len_sum_inter + len_inter
ave_c = c / len_filename
force_inter_array.append(ave_c)
len_inter_array.append(len_sum_inter)
print("AVE_force10= ", c/len(filenames10))
print("AVE_rate10= ", d/len(filenames10), "%")
percent_inter_array.append(d/len(filenames10))

c = 0
d = 0
len_filename = 0
len_inter = 0
for filename in filenames11:
    data = np.loadtxt(filename, delimiter=",")
    force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
    rate = (len(data[abs(data[:,1]) > 0.1, 1])/len(data[:,1]))*100
    c = c + force
    d = d + rate
    len_filename = len_filename + len(data[:,1])
    len_inter = len_inter + len(data[abs(data[:,1]) > 0.1, 1])
print(c)
len_sum_inter = len_sum_inter + len_inter
ave_c = c / len_filename
force_inter_array.append(ave_c)
len_inter_array.append(len_sum_inter)
print("AVE_force11= ", c/len(filenames11))
print("AVE_rate11= ", d/len(filenames11), "%")
percent_inter_array.append(d/len(filenames11))
#
# c = 0
# d = 0
# len_filename = 0
# len_inter = 0
# for filename in filenames12:
#     data = np.loadtxt(filename, delimiter=",")
#     force = sum(abs(data[abs(data[:, 1]) > 0.1, 1]))
#     rate = (len(data[abs(data[:, 1]) > 0.1, 1])/len(data[:, 1]))*100
#     c = c + force
#     d = d + rate
#     len_filename = len_filename + len(data[:, 1])
#     len_inter = len_inter + len(data[abs(data[:, 1]) > 0.1, 1])
# print(c)
# len_sum_inter = len_sum_inter + len_inter
# ave_c = c / len_filename
# force_inter_array.append(ave_c)
# len_inter_array.append(len_sum_inter)
# print("AVE_force12= ", c/len(filenames12))
# print("AVE_rate12= ", d/len(filenames12), "%")
# percent_inter_array.append(d/len(filenames12))
#
# c = 0
# d = 0
# len_filename = 0
# len_inter = 0
# for filename in filenames13:
#     data = np.loadtxt(filename, delimiter=",")
#     force = sum(abs(data[abs(data[:, 1]) > 0.1, 1]))
#     rate = (len(data[abs(data[:, 1]) > 0.1, 1])/len(data[:, 1]))*100
#     c = c + force
#     d = d + rate
#     len_filename = len_filename + len(data[:, 1])
#     len_inter = len_inter + len(data[abs(data[:, 1]) > 0.1, 1])
# print(c)
# len_sum_inter = len_sum_inter + len_inter
# ave_c = c / len_filename
# force_inter_array.append(ave_c)
# len_inter_array.append(len_sum_inter)
# print("AVE_force13= ", c/len(filenames13))
# print("AVE_rate13= ", d/len(filenames13), "%")
# percent_inter_array.append(d/len(filenames13))
#
# c = 0
# d = 0
# len_filename = 0
# len_inter = 0
# for filename in filenames14:
#     data = np.loadtxt(filename, delimiter=",")
#     force = sum(abs(data[abs(data[:, 1]) > 0.1, 1]))
#     rate = (len(data[abs(data[:, 1]) > 0.1, 1])/len(data[:, 1]))*100
#     c = c + force
#     d = d + rate
#     len_filename = len_filename + len(data[:, 1])
#     len_inter = len_inter + len(data[abs(data[:, 1]) > 0.1, 1])
# print(c)
# len_sum_inter = len_sum_inter + len_inter
# ave_c = c / len_filename
# force_inter_array.append(ave_c)
# len_inter_array.append(len_sum_inter)
# print("AVE_force14= ", c/len(filenames14))
# print("AVE_rate14= ", d/len(filenames14), "%")
# percent_inter_array.append(d/len(filenames14))

print(force_array)
print(len_array)
print(force_inter_array)
print(len_inter_array)
print(percent_array)
print(percent_inter_array)

# plt.plot(force_array)
# plt.plot(len_array)

fig, ax1 = plt.subplots()
x = np.array(range(1, 5))

color = 'tab:orange'
ax1.set_ylabel("torque[N.m]", color=color)
ax1.plot(x, force_array, color=color, label="torque(all_data)")
ax1.plot(x, force_inter_array, linestyle = "dashed", color=color, label="torque(selected_data)")
ax1.set_ylim(0, 0.15)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:green'
ax2.set_ylabel('frame for learning', color=color)
ax2.plot(x, len_array[:-1], color=color, label="frame(all_data)")
ax2.plot(x, len_inter_array[:-1], linestyle = "dashed", color=color, label="frame(selected_data)")
ax2.set_ylim(0, 10000)
ax2.tick_params(axis='y', labelcolor=color)

color = 'tab:purple'
ax1.set_xlabel('number of learning',color=color)
ax1.tick_params(axis='x', labelcolor=color)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

ax1.legend()
ax2.legend()
fig.tight_layout()
plt.show()
