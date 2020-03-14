import numpy as np

filename = "/media/tomoya/Tomoya's_T5/201910master/output_2019-11-02-16-45-00/image/video_color/force.csv"
force = np.loadtxt(filename)

print(force[force<-0.03])

list_index = []
list_force = []
for i in range(len(force)):
    if force[i] < -0.03:
        list_index.append(i)

print(list_index)
