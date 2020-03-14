#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import glob
import random
import cv2

filenames = ["/media/tomoya/Tomoya's_T5/201910master/output_2019-11-04-12-55-46/image",
	         "/media/tomoya/Tomoya's_T5/201910master/output_2019-11-04-12-56-18/image"]

train_image_dataset = []
test_image_dataset = []
train_vel_dataset = []
test_vel_dataset = []
train_num = []
test_num = []

for filename in filenames:
    train_image_list = []
    train_vel_list = []
    test_image_list = []
    test_vel_list = []
    image_file = glob.glob(filename+"/video_depth/*.png")
    image_file.sort()
    vel_file = np.loadtxt(filename+"/video_color/twist.csv")
    for i in range(min(len(image_file), len(vel_file))):
        if (i % 4 == 0):
            #print(image_file[i])
            train_image_list.append(image_file[i])
            train_vel_list.append(vel_file[i])
        else:
            test_image_list.append(image_file[i])
            test_vel_list.append(vel_file[i])

    train_num.append(min(len(train_image_list), len(train_vel_list)))
    test_num.append(min(len(train_image_list), len(test_vel_list)))
    train_image_dataset.append(train_image_list)
    train_vel_dataset.append(train_vel_list)
    test_image_dataset.append(test_image_list)
    test_vel_dataset.append(test_vel_list)

print(train_image_dataset[1][1])
print(train_vel_dataset[0])
print(test_image_dataset[1][1])
print(test_vel_dataset[0])


def make_dataset(image_dataset_all, vel_dataset_all, num):
    vel = []
    image_dataset = []
    vel_dataset = []

    for i in range(len(image_dataset_all)):
        image_file = image_dataset_all[i]
		#image_file.sort()
		#vel = np.loadtxt(filename+"/video_color/twist.csv")
        random_seq = range(num[i])
        random.shuffle(random_seq)

		#for l in range(len(random_seq)):
        for l in range(int(len(random_seq) * 0.6)): #メモリ足らないときに調整
			image = cv2.imread(image_file[random_seq[l]], flags=-1)
			image[image >= 5000] = 5000
			#image = image * 6.5535
			image = image * 13.107
			image = np.round(image)
			image = np.array(image, dtype="uint16")
			image_r = np.fliplr(image)
			image = np.reshape(image, [66, 200, 1])
			image_r = np.reshape(image, [66, 200, 1])
			image_dataset.append(image)
			image_dataset.append(image_r)

			vel_sample = vel_dataset_all[i][random_seq[l]]
			vel_dataset.append(vel_sample)
			vel_dataset.append(vel_sample)


    	#print np.asarray(train_image).shape
        print np.mean(np.asarray(vel_dataset))

	image_dataset = np.asarray(image_dataset)/65535.0 #たぶんtrain_imageがRBGの値だから正規化してる
	print(image_dataset.shape)
	vel_dataset = np.asarray(vel_dataset).reshape((len(vel_dataset),1))

	return image_dataset, vel_dataset

train_image, train_vel = make_dataset(train_image_dataset, train_vel_dataset, train_num)
