import matplotlib.pyplot as plt
import numpy as np

filename = "/home/tomoya/for0116/CNN/loss/0111-0-2-0.txt"
#f = open(filename)
#data1 = f.read()
#f.close()
#data1 = np.array(data1)
data1 = np.loadtxt(filename, delimiter=",")
#data1 = np.array(data1)
plt.plot(data1[:, 0], data1[:, 1])
plt.tick_params(labelsize = 12)
plt.xlabel("epoch", fontsize=15)
plt.ylabel("loss", fontsize=15)
plt.tight_layout()
#plt.rcParams["font.size"] = 25
plt.show()
