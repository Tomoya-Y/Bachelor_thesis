#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import cv2
import random
import glob
import numpy as np
import matplotlib.pyplot as plt
import copy


def make_dataset(image_dataset_all, steer_dataset_all, vel_dataset_all, num):
	steer = []
	image_dataset = []
	steer_dataset = []
	vel_dataset = []
	twist_dataset = []

	for i in range(len(image_dataset_all)):
		image_file = image_dataset_all[i]
		random_seq = range(num[i])
		random.shuffle(random_seq)

		for l in range(int(len(random_seq))): #メモリ足らないときに調整
			image = cv2.imread(image_file[random_seq[l]], flags=-1)
			image = np.reshape(image, [150, 150, 1])
			image_dataset.append(image)

			steer_sample = steer_dataset_all[i][random_seq[l]]
			steer_dataset.append(steer_sample)

			vel_sample = vel_dataset_all[i][random_seq[l]]
			vel_dataset.append(vel_sample)

	image_dataset = np.asarray(image_dataset)/255.0
	print(image_dataset.shape)
	steer_dataset = np.asarray(steer_dataset).reshape((len(steer_dataset),1))
	vel_dataset = np.asarray(vel_dataset).reshape((len(vel_dataset),1))
	twist_dataset.append(steer_dataset)
	twist_dataset.append(vel_dataset)
	twist_dataset = np.asarray(twist_dataset)
	twist_dataset = twist_dataset.transpose((1,0,2))
	print(twist_dataset.shape)

	return image_dataset, steer_dataset, vel_dataset, twist_dataset


def weight_variable(shape):
    # --- define weight
    initial = tf.random.truncated_normal(shape, stddev=0.1)#TODO
    return tf.Variable(initial)

def bias_variable(shape):
    # --- define bias
    initial = tf.constant(0.1, shape=shape)#TODO
    return tf.Variable(initial)

def conv1d(x, W):
    # --- define convolution
    return tf.nn.conv2d(x, W, strides=[1, 2, 2, 1], padding='VALID')

def conv2d(x, W):
    # --- define convolution
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='VALID')

def lrelu(x):
    x1 = tf.maximum(x,x/5.5)
    return x1


def CNN(image, vel, keep_prob):
	with tf.name_scope('norm1') as scope:
		norm1=tf.nn.lrn(image,4,bias=1.0,alpha=0.001/9.0,beta=0.75)

	with tf.name_scope('conv1') as scope:
		W_conv1 = weight_variable([5, 5, 1, 24])
		b_conv1 = bias_variable([24])
		h_conv1 = tf.nn.relu(conv1d(norm1, W_conv1) + b_conv1)
		print(h_conv1.shape)

	with tf.name_scope('conv2') as scope:
		W_conv2 = weight_variable([5, 5, 24, 36])
		b_conv2 = bias_variable([36])
		h_conv2 = tf.nn.relu(conv1d(h_conv1, W_conv2) + b_conv2)
		print(h_conv2.shape)

	with tf.name_scope('conv3') as scope:
		W_conv3 = weight_variable([5, 5, 36, 48])
		b_conv3 = bias_variable([48])
		h_conv3 = tf.nn.relu(conv1d(h_conv2, W_conv3) + b_conv3)
		print(h_conv3.shape)

	with tf.name_scope('conv4') as scope:
		W_conv4 = weight_variable([3, 3, 48, 64])
		b_conv4 = bias_variable([64])
		h_conv4 = tf.nn.relu(conv2d(h_conv3, W_conv4) + b_conv4)
		print(h_conv4.shape)

	with tf.name_scope('conv5') as scope:
		W_conv5 = weight_variable([3, 3, 64, 64])
		b_conv5 = bias_variable([64])
		h_conv5 = tf.nn.relu(conv2d(h_conv4, W_conv5) + b_conv5)
		print(h_conv5.shape)

	h_conv5_flatten = tf.reshape(h_conv5, [-1,9216])
	#
	# with tf.name_scope('fc1') as scope:
	# 	W_fc1 = weight_variable([9216, 100])
	# 	W_fc1_vel = weight_variable([1, 100])
	# 	b_fc1 = bias_variable([100])
	# 	h_fc1 = tf.nn.relu(tf.matmul(h_conv5_flatten, W_fc1) + b_fc1)
	# 	# h_fc1 = tf.nn.relu(tf.matmul(h_conv5_flatten, W_fc1) + tf.matmul(vel, W_fc1_vel) + b_fc1)
	#
	# with tf.name_scope('fc2') as scope:
	# 	W_fc2 = weight_variable([100,100])
	# 	b_fc2 = bias_variable([100])
	# 	h_fc2 = tf.nn.relu(tf.matmul(h_fc1, W_fc2) + b_fc2)

	with tf.name_scope('fc1') as scope:
		W_fc1 = weight_variable([9216, 100])
		W_fc1_vel = weight_variable([1, 100])
		b_fc1 = bias_variable([100])
		h_fc1 = tf.nn.relu(tf.matmul(h_conv5_flatten, W_fc1) + b_fc1)
		# h_fc1 = tf.nn.relu(tf.matmul(h_conv5_flatten, W_fc1) + tf.matmul(vel, W_fc1_vel) + b_fc1)

	with tf.name_scope('fc2') as scope:
		W_fc2 = weight_variable([100,100])
		b_fc2 = bias_variable([100])
		h_fc2 = tf.nn.relu(tf.matmul(h_fc1, W_fc2) + b_fc2)

	with tf.name_scope('fc3') as scope:
		W_fc3 = weight_variable([100,50])
		b_fc3 = bias_variable([50])
		h_fc3 = tf.nn.relu(tf.matmul(h_fc2, W_fc3) + b_fc3)

	with tf.name_scope('fc4') as scope:
		W_fc4 = weight_variable([50,10])
		b_fc4 = bias_variable([10])
		h_fc4 = tf.nn.relu(tf.matmul(h_fc3, W_fc4) + b_fc4)

	h_fc4_drop = tf.nn.dropout(h_fc4, rate = 1 - keep_prob)

	with tf.name_scope('fc5') as scope:
		W_fc5 = weight_variable([10,2])
		b_fc5 = bias_variable([2])
		y_conv = tf.matmul(h_fc4_drop, W_fc5) + b_fc5

	return y_conv,W_fc1


image1 = tf.compat.v1.placeholder(tf.float32, [None, 150, 150, 1])
vel1 = tf.compat.v1.placeholder(tf.float32, [None, 1])
y_twist = tf.compat.v1.placeholder(tf.float32, [None, 2, 1])
keep_prob = tf.compat.v1.placeholder(tf.float32)

y_conv,W_fc1 = CNN(image1, vel1, keep_prob)

loss = 0*tf.sqrt(tf.reduce_mean(tf.square(y_conv[:,0] - y_twist[:,0,0]))) + tf.sqrt(tf.reduce_mean(tf.square(y_conv[:,1] - y_twist[:,1,0])))
train_step = tf.compat.v1.train.AdamOptimizer(0.001).minimize(loss)

saver = tf.compat.v1.train.Saver(keep_checkpoint_every_n_hours = 1.0)

sess = tf.compat.v1.InteractiveSession()
sess.run(tf.compat.v1.global_variables_initializer())


# answer_file = "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-18-38-08"
# filenames = [
# "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-18-38-41"
# ]

answer_file = "/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-20-48-13"
filenames = [
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-20-45-10",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-20-45-34",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-20-45-56",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-20-46-20",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-20-46-41",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-20-47-08",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-20-47-29",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-20-47-52",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-21-12",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-21-37",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-22-37",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-23-00",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-23-21",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-24-53",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-25-17",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-26-25",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-26-49",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-27-35",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-21-28-03",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-05-55",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-06-19",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-06-43",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-07-04",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-07-27",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-07-50",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-08-14",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-08-38",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-09-01",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-09-25",
"/media/tomoya/Tomoya's_T5/sotsuron_data/outputlog_2020-02-26-22-10-41"
]



train_image_dataset = []
test_image_dataset = []
train_steer_dataset = []
test_steer_dataset = []
train_vel_dataset = []
test_vel_dataset = []
train_num = []
test_num = []

s_train_image_list = []
s_train_steer_list = []
s_train_vel_list = []
s_test_image_list = []
s_test_steer_list = []
s_test_vel_list = []
s_image_file = glob.glob(answer_file+"/image/*.png")
s_image_file.sort()
s_twist_file = np.loadtxt(answer_file+"/twist.csv", delimiter=",", usecols=[1,2])
s_twist_file[abs(s_twist_file[:,0]) > 1, 0] = 0
s_vel2_file = copy.copy(s_twist_file[:,1])
s_vel2_file = np.insert(s_vel2_file, 0, 0)
s_vel2_file = s_vel2_file[:-1]
s_accel_file = s_twist_file[:,1] - s_vel2_file
for i in range(len(s_image_file)):
	if (i%4==0):
		s_test_image_list.append(s_image_file[i])
		s_test_steer_list.append(s_twist_file[i,0])
		s_test_vel_list.append(s_twist_file[i,1])
	else:
		s_train_image_list.append(s_image_file[i])
		s_train_steer_list.append(s_twist_file[i,0])
		s_train_vel_list.append(s_twist_file[i,1])
train_num.append(len(s_train_image_list))
test_num.append(len(s_test_image_list))
train_image_dataset.append(s_train_image_list)
train_steer_dataset.append(s_train_steer_list)
train_vel_dataset.append(s_train_vel_list)
test_image_dataset.append(s_test_image_list)
test_steer_dataset.append(s_test_steer_list)
test_vel_dataset.append(s_test_vel_list)

#separate train and test dataset
for filename in filenames:
	train_image_list = []
	train_steer_list = []
	train_vel_list = []
	test_image_list = []
	test_steer_list = []
	test_vel_list = []

	image_file = glob.glob(filename+"/image/*.png")
	image_file.sort()
	twist_file = np.loadtxt(filename+"/twist.csv", delimiter=",", usecols=[1,2])
	vel2_file = copy.copy(twist_file[:,1])
	vel2_file = np.insert(vel2_file, 0, 0)
	vel2_file = vel2_file[:-1]
	accel_file = twist_file[:,1] - vel2_file
	twist_file[abs(twist_file[:,0]) > 1, 0] = 0
	force_file = np.loadtxt(filename+"/force.csv", delimiter=",", usecols=[1,2])
	force_index = []
	noforce_index = []
	for i in range(len(force_file)):
		if (abs(force_file[i,0]) > 0.1) or (abs(force_file[i,1]) > 0.1):
			force_index.append(i)
		else:
			noforce_index.append(i)
	print(len(force_index))
	k = 0
	for i in force_index:
		if (k % 4 == 0):
			test_image_list.append(image_file[i])
			test_steer_list.append(twist_file[i,0])
			test_vel_list.append(twist_file[i,1])
		else:
			train_image_list.append(image_file[i])
			train_steer_list.append(twist_file[i,0])
			train_vel_list.append(twist_file[i,1])
		k += 1

	train_num.append(len(train_image_list))
	test_num.append(len(test_image_list))
	train_image_dataset.append(train_image_list)
	train_steer_dataset.append(train_steer_list)
	train_vel_dataset.append(train_vel_list)
	test_image_dataset.append(test_image_list)
	test_steer_dataset.append(test_steer_list)
	test_vel_dataset.append(test_vel_list)


l=0
trainrmse = 4
batchSize = 32

while(l<=10000):

	train_image, train_steer, train_vel, train_twist = make_dataset(train_image_dataset, train_steer_dataset, train_vel_dataset, train_num)
	test_image, test_steer, test_vel, test_twist = make_dataset(test_image_dataset, test_steer_dataset, test_vel_dataset, test_num)
	itter = train_image.shape[0]/batchSize
	random_seq = range(train_image.shape[0])

	print ("finish making dataset")
	random.shuffle(random_seq)
	rmse_list = []
	for i in range(itter):
		l += 1
		sess.run(train_step,feed_dict={image1:train_image[random_seq[i*batchSize:(i+1)*batchSize],:,:,:], vel1:train_vel[random_seq[i*batchSize:(i+1)*batchSize],:], y_twist:train_twist[random_seq[i*batchSize:(i+1)*batchSize],:,:], keep_prob: 0.5})#TODO default0.5

		if(l>=10000):
			break

		if(l%100 == 0):
			rmse = sess.run(loss, feed_dict={image1: test_image, vel1:test_vel, y_twist:test_twist, keep_prob:1.0})
			f = open("loss/0301test.txt","a")
			if(rmse<trainrmse):
				trainrmse=rmse
				save_path = saver.save(sess, "model/0301test.ckpt")

				f.write("%d, %f\n" %(l,rmse))
				print("epoch:=%d ,test_acc:=%f ModelSave!\n" %(l,rmse))
			else:
			   f.write("%d, %f\n" %(l,rmse))
			   print("epoch:=%d ,test_acc:=%f\n" %(l,rmse))
			rmse_list.append(rmse)
			f.close()
