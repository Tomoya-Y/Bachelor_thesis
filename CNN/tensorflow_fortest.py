import rospy
from sensor_msgs.msg import Image
# from sensor_msgs.msg import ImagePtr
from sensor_msgs.msg import Joy
from cv_bridge import CvBridge
import cv2
import numpy as np
import tensorflow as tf
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped
import time
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32


def weight_variable(shape):
    # --- define weight
    initial = tf.random.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    # --- define bias
    initial = tf.constant(0.1, shape=shape)
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


def CNN(image, vel):
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

    h_conv5_flatten = tf.reshape(h_conv5, [-1,960])

    with tf.name_scope('fc1') as scope:

        W_fc1 = weight_variable([960, 1164])
        W_fc1_vel = weight_variable([1, 1164])
        b_fc1 = bias_variable([1164])
        h_fc1 = tf.nn.relu(tf.matmul(h_conv5_flatten, W_fc1) + b_fc1)
        # h_fc1 = tf.nn.relu(tf.matmul(h_conv5_flatten, W_fc1) + tf.matmul(vel, W_fc1_vel) + b_fc1)

    with tf.name_scope('fc2') as scope:
        W_fc2 = weight_variable([1164,100])
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

    h_fc4_drop = tf.nn.dropout(h_fc4, rate=0)

    with tf.name_scope('fc5') as scope:
        W_fc5 = weight_variable([10,2])
        b_fc5 = bias_variable([2])
        y_conv = tf.matmul(h_fc4_drop, W_fc5) + b_fc5
        # y_conv_list = []
        # y_conv_list.append([y_conv[0]])
        # y_conv_list.append([y_conv[1]])
        # y_conv = y_conv_list


    return y_conv


class RosTensorFlow():
    def __init__(self):
        self.sub_image0_flag=0
        self.sub_twist0_flag=0
        self.cv_image = np.zeros((80,100,1), np.uint8)
        self.cv_image1 = np.zeros((1,80,100,1), np.uint8)


        # self.twist = Twist()

        self._cv_bridge = CvBridge()
        self._sub1 = rospy.Subscriber('/image_move', Image, self.callback_image, queue_size=1)
        self._sub2 = rospy.Subscriber('/ypspur_ros/cmd_vel', Twist, self.callback_twist, queue_size=1)
        self._pub1 = rospy.Publisher('/tomoyakun', Twist, queue_size=1)#TODO
        # self._pub2 = rospy.Publisher('/tomoyakun2', Twist, queue_size=1)#TODO
        # self._pub3 = rospy.Publisher('/image_pub', Float32, queue_size=1)#TODO

        self.x = tf.compat.v1.placeholder(tf.float32, [None,80,100,1], name="x")
        self.vel = tf.compat.v1.placeholder(tf.float32, [None,1])

        self.y_conv  = CNN(self.x, self.vel)
        # y_conv_list = []
        # y_conv_list.append([self.y_conv1[:,0]])
        # y_conv_list.append([self.y_conv1[:,1]])
        # self.y_conv = np.array(y_conv_list)

        self._session = tf.compat.v1.InteractiveSession()
        self._saver = tf.compat.v1.train.Saver()
        self._session.run(tf.compat.v1.global_variables_initializer())
        self._saver.restore(self._session, "model/0226-1-2-0.ckpt")

    def callback(self):

         if(self.sub_image0_flag==1):
             # t1 = time.time()
             self.sub_image0_flag=0
             self.sub_twist0_flag=0
             # list_image = []
             # cv_image = self._cv_bridge.imgmsg_to_cv2(self.image_msg0, "mono8")
             # cv_image = np.reshape(cv_image, [80, 100, 1])/255.0
             # list_image.append(self.cv_image)
             # self._steer = self._session.run(self.y_conv, feed_dict={self.x:list_image})
             # print(self.cv_image)
             vel = [[self.twist_now.linear.x]]
             self._twist = self._session.run(self.y_conv, feed_dict={self.x:self.cv_image1, self.vel:vel})

             image_steer = self._twist[:,0]
             image_vel = self._twist[:,1]
             twist = Twist()
             # if image_vel < 0.1:
             #     twist.linear
             twist.linear.x = image_vel
             twist.angular.z = image_steer
             self._pub1.publish(twist)
             # self._pub2.publish(self.twist)
             # self._pub3.publish(float(self.cv_image1.shape[0])/5)
             # t2 = time.time()
             print self._twist
             # print(t2-t1)


    def callback_image(self,image_msg):
        self.sub_image0_flag=1
        self.cv_image = self._cv_bridge.imgmsg_to_cv2(image_msg, "mono8")
        self.cv_image1 = np.reshape(self.cv_image, [1, 80, 100, 1])/255.0
        # self.image_msg0 = image_msg
        self.callback()

    def callback_twist(self,twist_msg):
        self.sub_twist0_flag=1
        self.twist_now = twist_msg
        self.callback()


    def main(self):
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node('rostensorflow')
    tensor = RosTensorFlow()
    tensor.main()
