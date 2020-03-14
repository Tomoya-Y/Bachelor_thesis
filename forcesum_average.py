import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as ticker
import japanize_matplotlib


force_array = []
len_array = []
force_inter_array = []
len_inter_array = []
percent_array = []
percent_inter_array = []

# force_array.append([0.10653080129689671, 0.11904761904761904, 0.12311780336581045])
# len_array.append([1081, 3240, 5508])
# force_inter_array.append([0.10653080129689671, 0.12742504409171077, 0.1078167115902965])
# len_inter_array.append([1081, 1818, 2786])
# percent_array.append([33, 36, 41])
# percent_inter_array.append([33, 42, 35])
#
# force_array.append([0.1259698767685988, 0.12263736263736263, 0.09838337182448037])
# len_array.append([1078, 3269, 5544])
# force_inter_array.append([0.1259698767685988, 0.1273966766084363, 0.10959507042253522])
# len_inter_array.append([1078, 1947, 2934])
# percent_array.append([39, 38, 31])
# percent_inter_array.append([39, 41, 35])
#
# force_array.append([0.10818438381937912, 0.09743824336688015, 0.13312130849613812])
# len_array.append([1096, 3222, 5408])
# force_inter_array.append([0.10818438381937912, 0.13392857142857142, 0.12477396021699819])
# len_inter_array.append([1096, 1818, 2812])
# percent_array.append([33, 31, 44])
# percent_inter_array.append([33, 43, 40])

force_array.append([0.12220540610205134, 0.14306056845238066, 0.11609737777777795, 0.08082304866803279])
len_array.append([973, 2874, 4890, 6825, 8777])
force_inter_array.append([0.12220540610205134, 0.14147839321674624, 0.1001663286965481, 0.11787890749354007])
len_inter_array.append([973, 1866, 2901, 3715, 4596])
percent_array.append([47.007486955385986, 53.714663026820865, 45.855910619586254, 34.83023110424646])
percent_inter_array.append([47.007486955385986, 54.8514907097441, 41.95388081506459, 45.52632085088378])

force_array.append([0.14479627442094617, 0.12442559556494194, 0.12636668491048603, 0.1368512516455696])
len_array.append([982, 2968, 4862, 6817, 8792])
force_inter_array.append([0.14479627442094617, 0.11848036973894509, 0.09936559928534965, 0.13144558996897612])
len_inter_array.append([982, 2059, 3021, 3825, 4800])
percent_array.append([54.21115943557744, 50.56713768309872, 47.520818592499865, 50.762578519585276])
percent_inter_array.append([54.21115943557744, 51.25264539451574, 41.004296399446325, 50.39495636550308])

force_array.append([0.11408910387513461, 0.1253219739696314, 0.13303267014613768, 0.15478887863334972])
len_array.append([988, 2846, 4690, 6606, 8567])
force_inter_array.append([0.11408910387513461, 0.08648962615859943, 0.07625414024071163, 0.12532329399477804])
len_inter_array.append([988, 1813, 2560, 3226, 4116])
percent_array.append([44.39797431975154, 47.540057880991036, 51.29043154218718, 57.8859008044736])
percent_inter_array.append([44.39797431975154, 38.45933562428408, 34.82097859193199, 46.46351439790576])

force_array = np.array(force_array)
len_array = np.array(len_array)
force_inter_array = np.array(force_inter_array)
len_inter_array = np.array(len_inter_array)
percent_array = np.array(percent_array)
percent_inter_array = np.array(percent_inter_array)

force_array = np.mean(force_array, axis=0)
len_array = np.mean(len_array, axis=0)
force_inter_array = np.mean(force_inter_array, axis=0)
len_inter_array = np.mean(len_inter_array, axis=0)
percent_array = np.mean(percent_array, axis=0)
percent_inter_array = np.mean(percent_inter_array, axis=0)

fig, ax1 = plt.subplots()
x = np.array(range(1, 5))

igfont = {'family':'IPAexGothic'}

color = 'tab:orange'
ax1.set_ylabel("トルク[N・m]", color=color, fontsize=14)
# ax1.plot(x, force_array*2.5, color=color, label="トルク(全データ)")
# ax1.plot(x, force_inter_array*2.5, linestyle = "dashed", color=color, label="トルク(介入データ)")
ax1.plot(x, force_array*2.5, color=color)
ax1.plot(x, force_inter_array*2.5, linestyle = "dashed", color=color)
ax1.set_ylim(0)
ax1.tick_params(axis='y', labelcolor=color, labelsize=14)

ax2 = ax1.twinx()

color = 'tab:green'
ax2.set_ylabel('データ数', color=color, fontsize=14)
# ax2.plot(x, len_array[:-1], color=color, label="データ数(全データ)")
# ax2.plot(x, len_inter_array[:-1], linestyle = "dashed", color=color, label="データ数(介入データ)")
ax2.plot(x, len_array[:-1], color=color)
ax2.plot(x, len_inter_array[:-1], linestyle = "dashed", color=color)
ax2.set_ylim(0, 10000)
ax2.tick_params(axis='y', labelcolor=color, labelsize=14)

color = 'tab:purple'
ax1.set_xlabel('学習回数[回]',color=color, fontsize=14)
ax1.tick_params(axis='x', labelcolor=color, labelsize=14)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

ax1.legend(loc='upper left', fontsize=14)
ax2.legend(loc = 'best', fontsize=14)
fig.tight_layout()
plt.show()

plt.plot(x, percent_array, label='all_data')
plt.plot(x, percent_inter_array, label="selected_data")
plt.xlabel("number of learning")
plt.ylabel("percentage of intervention[%]")
plt.ylim(0, 50)
plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
plt.legend()
plt.tight_layout()
plt.show()
