import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as ticker
import japanize_matplotlib


first_file = "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-20-33-52"
first_force = np.loadtxt(first_file+"/moveforce.csv", delimiter=",", usecols=1)

#from filenames1 to filenames3: learn from all data
all_file = []
filenames0 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-20-40-46",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-20-43-41",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-20-44-40",
]
all_file.append(filenames0)

filenames1 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-20-59-50",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-01-01",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-01-52"
]
all_file.append(filenames1)

filenames2 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-28-52",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-29-41",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-30-30"
]
all_file.append(filenames2)

filenames3 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-54-26",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-55-21",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-56-11"
]
all_file.append(filenames3)

# filenames4 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-10-13-09",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-10-14-17",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-10-15-26",
# ]
# all_file.append(filenames4)
#
# filenames5 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-14-01",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-15-12",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-16-20",
# ]
# all_file.append(filenames5)
#
# filenames6 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-46-56",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-48-03",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-49-11",
# ]
# all_file.append(filenames6)
#
# filenames7 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-15-21-34",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-15-22-42",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-15-23-56",
# ]
# all_file.append(filenames7)
#
# filenames8 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-01-19",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-02-26",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-03-45",
# ]
# all_file.append(filenames8)
#
# filenames9 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-37-40",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-38-47",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-40-06",
# ]
# all_file.append(filenames9)
#
# filenames10 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-17-12-13",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-17-15-42",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-17-16-48",
# ]
# all_file.append(filenames10)
#
# filenames11 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-18-09-46",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-18-10-53",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-18-12-06",
# ]
# all_file.append(filenames11)
#
# filenames12 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-13-42-33",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-13-43-43",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-13-44-50",
# ]
# all_file.append(filenames12)
#
# filenames13 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-14-04-42",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-14-05-45",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-14-06-49",
# ]
# all_file.append(filenames13)
#
# filenames14 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-16-40-56",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-16-42-01",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-16-43-07",
# ]
# all_file.append(filenames14)
#
# filenames15 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-16-59-39",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-00-45",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-01-50",
# ]
# all_file.append(filenames15)
#
# filenames16 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-18-07",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-19-13",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-20-22",
# ]
# all_file.append(filenames16)
#
# filenames17 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-56-08",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-57-16",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-58-19",
# ]
# all_file.append(filenames17)
#
# filenames18 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-19-10",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-20-21",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-21-27",
# ]
# all_file.append(filenames18)
#
# filenames19 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-41-31",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-42-36",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-43-38",
# ]
# all_file.append(filenames19)


#from filenames4 to filenames6: learn from intervention data
inter_file = []
filenames20 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-20-40-46",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-20-43-41",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-20-44-40",
]
inter_file.append(filenames20)

filenames21 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-03-10",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-04-00",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-04-53"
]
inter_file.append(filenames21)

filenames22 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-31-35",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-34-43",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-35-31"
]
inter_file.append(filenames22)

filenames23 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-57-12",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-57-59",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-23-21-58-47"
]
inter_file.append(filenames23)

# filenames24 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-10-16-55",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-10-18-03",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-10-19-09",
# ]
# inter_file.append(filenames24)
#
# filenames25 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-20-54",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-22-02",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-23-32",
# ]
# inter_file.append(filenames25)
#
# filenames26 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-50-37",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-51-49",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-11-52-58",
# ]
# inter_file.append(filenames26)
#
# filenames27 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-15-26-42",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-15-27-48",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-15-29-00",
# ]
# inter_file.append(filenames27)
#
# filenames28 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-05-25",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-06-35",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-07-42",
# ]
# inter_file.append(filenames28)
#
# filenames29 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-41-31",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-42-39",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-16-43-46",
# ]
# inter_file.append(filenames29)
#
# filenames30 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-17-18-14",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-17-19-21",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-17-20-36",
# ]
# inter_file.append(filenames30)
#
# filenames31 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-18-13-39",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-18-14-44",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-07-18-15-52",
# ]
# inter_file.append(filenames31)
#
# filenames32 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-13-47-18",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-13-48-29",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-13-50-58",
# ]
# inter_file.append(filenames32)
#
# filenames33 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-14-08-14",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-14-09-18",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-14-10-23",
# ]
# inter_file.append(filenames33)
#
# filenames34 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-16-44-32",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-16-45-39",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-16-46-45",
# ]
# inter_file.append(filenames34)
#
# filenames35 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-03-25",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-04-29",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-05-33",
# ]
# inter_file.append(filenames35)
#
# filenames36 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-21-50",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-23-00",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-24-05",
# ]
# inter_file.append(filenames36)
#
# filenames37 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-17-59-47",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-00-52",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-01-57",
# ]
# inter_file.append(filenames37)
#
# filenames38 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-22-54",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-23-59",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-25-02",
# ]
# inter_file.append(filenames38)
#
# filenames39 = ["/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-45-23",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-46-29",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-18-47-35",
# ]
# inter_file.append(filenames39)



steer_force_array = []
steer_force_inter_array = []
vel_force_array = []
vel_force_inter_array = []
len_array = []
len_inter_array = []
percent_array = []
percent_inter_array = []
# each_force = np.zeros((len(all_file), len(filenames0)))
each_force = []
len_sum = math.floor(len(first_force)*3/4)
len_array.append(len_sum)
count1=0
for filenames in all_file:
    steer_force_sum = 0
    vel_force_sum = 0
    inter_sum = 0
    learn_len_filename = 0
    len_filename = 0
    for filename in filenames:
        data = np.loadtxt(filename+"/moveforce.csv", delimiter=",")
        steer_force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
        vel_force = sum(abs(data[abs(data[:,2]) > 0.1, 2]))
        # inter_num=0
        # for i in len(data):
        #     if (abs(data[:,1])>0.1 or abs(data[:,2])>0.1):
        #         inter_num +=1
        inter_num = len(data[abs(data[:,1]) > 0.1, 1])
        steer_force_sum = steer_force_sum + steer_force
        vel_force_sum = vel_force_sum + vel_force
        inter_sum = inter_sum + inter_num
        learn_len_filename = learn_len_filename + math.floor(len(data[:,2])*3/4)
        len_filename = len_filename + len(data[:,1])
        # each_force_ave = force / len(data[:,1])
        # each_force.append([int(count1+1),each_force_ave])
    len_sum = len_sum + learn_len_filename
    ave_steer_force = steer_force_sum / len_filename
    ave_vel_force = vel_force_sum / len_filename
    ave_inter = inter_sum / len_filename
    steer_force_array.append(ave_steer_force)
    vel_force_array.append(ave_vel_force)
    len_array.append(len_sum)
    percent_array.append(ave_inter*100)
    # print("AVE_force"+str(count1)+"= ", force_sum/len(filenames))
    # print("AVE_rate"+str(count1)+"= ", rate_sum/len(filenames), "%")
    count1 +=1
# each_force = np.array(each_force)
# each_force = each_force.transpose()


len_sum_inter = math.floor(len(first_force)*3/4)
len_inter_array.append(len_sum_inter)
each_inter_force = []
count2 = 0
for filenames in inter_file:
    steer_force_sum = 0
    vel_force_sum = 0
    inter_sum = 0
    learn_len_filename = 0
    len_filename = 0
    learn_len_inter = 0
    len_inter = 0
    for filename in filenames:
        data = np.loadtxt(filename+"/moveforce.csv", delimiter=",")
        steer_force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
        steer_force = sum(abs(data[abs(data[:,2]) > 0.1, 2]))
        inter_num = len(data[abs(data[:,1]) > 0.1, 1])
        steer_force_sum = steer_force_sum + steer_force
        vel_force_sum = vel_force_sum + vel_force
        inter_sum = inter_sum + inter_num
        learn_len_filename = learn_len_filename + math.floor(len(data[:,1])*3/4)
        len_filename = len_filename + len(data[:,1])
        learn_len_inter = learn_len_inter + math.floor(len(data[abs(data[:,1]) > 0.1, 1])*3/4)
        len_inter = len_inter + len(data[abs(data[:,1]) > 0.1, 1])
        # each_inter_force.append([int(count2+1), force/len(data[:,1])])
    len_sum_inter = len_sum_inter + learn_len_inter
    ave_steer_force = steer_force_sum / len_filename
    ave_vel_force = vel_force_sum / len_filename
    ave_inter = inter_sum / len_filename
    steer_force_inter_array.append(ave_steer_force)
    vel_force_inter_array.append(ave_vel_force)
    len_inter_array.append(len_sum_inter)
    percent_inter_array.append(ave_inter*100)
    # print("AVE_force"+str(count2)+"= ", force_sum/len(filenames))
    # print("AVE_rate"+str(count2)+"= ", rate_sum/len(filenames), "%")
    count2+=1
# each_inter_force = np.array(each_inter_force)
# each_inter_force = each_inter_force.transpose()

print(steer_force_array)
print(vel_force_array)
print(len_array)
print(steer_force_inter_array)
print(vel_force_inter_array)
print(len_inter_array)
print(percent_array)
print(percent_inter_array)
# print(each_force)
# print(each_inter_force)


fig, ax1 = plt.subplots()
x = np.array(range(1, 5))

igfont = {'family':'IPAexGothic'}

color = 'tab:blue'
ax1.set_ylabel("ハンドルに加わったトルクの平均値[N・m]", fontsize=20)
ax1.plot(x, np.array(steer_force_array)*2.5, linestyle = "dashed", color=color, label="ハンドルトルク(全走行シーン)", marker=".", ms=10)
ax1.plot(x, np.array(steer_force_inter_array)*2.5, color=color, label="ハンドルトルク(介入シーン)", marker=".", ms=10)
ax1.plot(x, np.array(vel_force_array)*2.5, linestyle = "dashed", color="tab:green", label="アクセルトルク(全走行シーン)", marker=".", ms=10)
ax1.plot(x, np.array(vel_force_inter_array)*2.5, color="tab:green", label="アクセルトルク(介入シーン)", marker=".", ms=10)
# ax1.scatter(each_force[0], each_force[1]*2.5, color=color, marker="^")
# ax1.scatter(each_inter_force[0], each_inter_force[1]*2.5, color=color)
ax1.set_ylim(0,0.35)
ax1.tick_params(axis='y', labelsize=20)

ax2 = ax1.twinx()

color = 'tab:orange'
ax2.set_ylabel('学習データ数', color="k", fontsize=20)
ax2.plot(x, len_array[:-1], linestyle = "dashed", color=color, label="データ数(全走行シーン)", marker=".", ms=10)
ax2.plot(x, len_inter_array[:-1], color=color, label="データ数(介入シーン)", marker="." ,ms=10)
ax2.set_ylim(0, 10000)
ax2.tick_params(axis='y', labelsize=20)

color = 'tab:purple'
ax1.set_xlabel('学習回数[回]', fontsize=20)
ax1.tick_params(axis='x', labelsize=20)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

ax1.legend(loc='upper left', fontsize=18)
ax2.legend(loc = 'upper right', fontsize=18)
fig.tight_layout()
plt.show()

# plt.plot(x, percent_array, label='all_data', marker=".", ms=10)
# plt.plot(x, percent_inter_array, label="selected_data", marker=".", ms=10)
# plt.xlabel("number of learning")
# plt.ylabel("percentage of intervention[%]")
# plt.ylim(0, 50)
# plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
# plt.legend()
# plt.tight_layout()
# plt.show()
