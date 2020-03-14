import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as ticker
import japanize_matplotlib

# file_all = []
# filename1 = [
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-20-58-28",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-00-44",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-02-57",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-05-32",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-06-38"
# ]
# file_all.append(filename1)
#
# filename2 = [
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-08-06",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-09-14",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-10-19",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-11-47",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-12-51"
# ]
# file_all.append(filename2)
#
# filename3 = [
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-14-07",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-16-59",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-18-05",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-19-21",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-20-27"
# ]
# file_all.append(filename3)
#
# file_inter = []
# filename4 = [
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-22-08",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-23-13",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-24-20",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-25-38",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-26-43"
# ]
# file_inter.append(filename4)
#
# filename5 = [
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-28-05",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-29-26",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-30-29",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-31-37",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-32-40"
# ]
# file_inter.append(filename5)
#
#
# filename6 = [
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-34-03",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-35-55",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-36-59",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-38-06",
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-08-21-39-12"
# ]
# file_inter.append(filename6)

file_all = []
filename1 = [
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-36-13",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-37-23",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-38-29",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-39-41",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-40-49"
]
file_all.append(filename1)

filename2 = [
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-43-10",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-44-19",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-45-24",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-46-42",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-20-47-59"
]
file_all.append(filename2)

filename3 = [
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-15-11",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-16-20",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-17-24",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-18-34",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-19-41"
]
file_all.append(filename3)

file_inter = []
filename4 = [
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-21-24",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-23-16",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-24-24",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-25-31",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-26-36"
]
file_inter.append(filename4)

filename5 = [
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-28-02",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-29-09",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-30-16",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-31-23",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-32-50"
]
file_inter.append(filename5)


filename6 = [
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-34-13",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-35-19",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-36-32",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-37-40",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-10-21-38-47"
]
file_inter.append(filename6)



force_array = []
force_inter_array = []
len_array = []
len_inter_array = []
percent_array = []
percent_inter_array = []


count1=0
for filenames in file_all:
    force_sum = 0
    inter_sum = 0
    learn_len_filename = 0
    len_filename = 0
    for filename in filenames:
        data = np.loadtxt(filename+"/moveforce.csv", delimiter=",")
        force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
        inter_num = len(data[abs(data[:,1]) > 0.1, 1])
        force_sum = force_sum + force
        inter_sum = inter_sum + inter_num
        learn_len_filename = learn_len_filename + math.floor(len(data[:,1])*3/4)
        len_filename = len_filename + len(data[:,1])
    ave_force = force_sum / len_filename
    ave_inter = inter_sum / len_filename
    force_array.append(ave_force)
    percent_array.append(ave_inter*100)
    # print("AVE_force"+str(count1)+"= ", force_sum/len(filenames))
    # print("AVE_rate"+str(count1)+"= ", rate_sum/len(filenames), "%")
    count1 +=1


count2 = 0
for filenames in file_inter:
    force_sum = 0
    inter_sum = 0
    learn_len_filename = 0
    len_filename = 0
    learn_len_inter = 0
    len_inter = 0
    for filename in filenames:
        data = np.loadtxt(filename+"/moveforce.csv", delimiter=",")
        force = sum(abs(data[abs(data[:,1]) > 0.1, 1]))
        inter_num = len(data[abs(data[:,1]) > 0.1, 1])
        force_sum = force_sum + force
        inter_sum = inter_sum + inter_num
        learn_len_filename = learn_len_filename + math.floor(len(data[:,1])*3/4)
        len_filename = len_filename + len(data[:,1])
        learn_len_inter = learn_len_inter + math.floor(len(data[abs(data[:,1]) > 0.1, 1])*3/4)
        len_inter = len_inter + len(data[abs(data[:,1]) > 0.1, 1])
    ave_force = force_sum / len_filename
    ave_inter = inter_sum / len_filename
    force_inter_array.append(ave_force)
    percent_inter_array.append(ave_inter*100)
    count2+=1

force_array_torque = np.array(force_array)*2.5
force_inter_array_torque = np.array(force_inter_array)*2.5

print(force_array_torque)
print(np.mean(force_array_torque))
print(force_inter_array_torque)
print(np.mean(force_inter_array_torque))


# fig, ax1 = plt.subplots()
# x = np.array(range(1, ))
#
# igfont = {'family':'IPAexGothic'}
#
# color = 'tab:orange'
# ax1.set_ylabel("トルク[N・m]", color=color, fontsize=14)
# ax1.plot(x, np.array(force_array)*2.5, color=color, label="トルク(全データ)", marker=".", ms=10)
# ax1.plot(x, np.array(force_inter_array)*2.5, linestyle = "dashed", color=color, label="トルク(介入データ)", marker=".", ms=10)
# ax1.set_ylim(0,0.3)
# ax1.tick_params(axis='y', labelcolor=color, labelsize=14)
#
# ax2 = ax1.twinx()
#
# color = 'tab:green'
# ax2.set_ylabel('学習データ数', color=color, fontsize=14)
# ax2.plot(x, len_array[:-1], color=color, label="データ数(全データ)", marker=".", ms=10)
# ax2.plot(x, len_inter_array[:-1], linestyle = "dashed", color=color, label="データ数(介入データ)", marker="." ,ms=10)
# ax2.set_ylim(0, 60000)
# ax2.tick_params(axis='y', labelcolor=color, labelsize=14)
#
# color = 'tab:purple'
# ax1.set_xlabel('学習回数[回]',color=color, fontsize=14)
# ax1.tick_params(axis='x', labelcolor=color, labelsize=14)
# ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
#
# ax1.legend(loc='upper left', fontsize=14)
# ax2.legend(loc = 'best', fontsize=14)
# fig.tight_layout()
# plt.show()

# plt.plot(x, percent_array, label='all_data', marker=".", ms=10)
# plt.plot(x, percent_inter_array, label="selected_data", marker=".", ms=10)
# plt.xlabel("number of learning")
# plt.ylabel("percentage of intervention[%]")
# plt.ylim(0, 50)
# plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
# plt.legend()
# plt.tight_layout()
# plt.show()
