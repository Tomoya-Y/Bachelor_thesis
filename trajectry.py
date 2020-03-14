import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches

# filenames0 = ["/media/tomoya/Tomoya's_T5/1125/1126121829.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126121852.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126121953.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126122034.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126122120.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126122154.csv",
# ]
#
# filenames1 = ["/media/tomoya/Tomoya's_T5/1125/1126132939.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126132959.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126133033.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126133112.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126133157.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126133237.csv",
# ]
#
# filenames2 = ["/media/tomoya/Tomoya's_T5/1125/1126142750.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126142837.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126142925.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126143010.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126143232.csv",
# "/media/tomoya/Tomoya's_T5/1125/1126143443.csv",
# ]

filenames0 = ["/media/tomoya/Tomoya's_T5/1127/1127212336.csv",
"/media/tomoya/Tomoya's_T5/1127/1127212422.csv",
"/media/tomoya/Tomoya's_T5/1127/1127212454.csv",
"/media/tomoya/Tomoya's_T5/1127/1127212553.csv"
]

filenames1 = ["/media/tomoya/Tomoya's_T5/1127/1127224318.csv",
"/media/tomoya/Tomoya's_T5/1127/1127224359.csv",
"/media/tomoya/Tomoya's_T5/1127/1127224452.csv",
"/media/tomoya/Tomoya's_T5/1127/1127224541.csv",
]

c = 0
color_list = ["b", "b", "g", "g", "r", "r"]
for filename in filenames1:
    data = np.loadtxt(filename, delimiter=",", skiprows=1, usecols=[5, 6, 10, 11, 48])

    start = data[:, 4]
    start = np.where(start != 0.0)
    start = start[0][3]
    print(start)
    x = data[start:, 0]
    y = data[start:, 1]
    x = x - data[start, 0]
    y = y - data[start, 1]
    # plt.plot(x, y, "b")
    # z = np.mean(data[start:start+10, 2])
    # w = np.mean(data[start:start+10, 3])
    z = np.mean(data[start, 2])
    w = np.mean(data[start, 3])
    # z = data[start, 2]
    # w = data[start, 3]
    theta = 2 * math.atan(abs(z) / w)

    theta = abs(theta)
    print(theta)
    xx = x*np.cos(theta) - y*np.sin(theta)
    yy = x*np.sin(theta) + y*np.cos(theta)

    # plt.plot(xx, yy, color_list[c])
    plt.plot(xx, yy, "b")
    c += 1

# plt.xlim(0, 5.0)
# plt.ylim(-1.14, 1.14)
plt.xlabel("forward distance [m]")
plt.ylabel("side distance [m]")
r = patches.Rectangle(xy=(2, -0.265), width=0.33, height=0.53, ec='k', fill=False)
plt.gca().add_patch(r)
plt.gca().set_aspect('equal')
plt.show()
