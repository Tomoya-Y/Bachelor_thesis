import rospy
import numpy as np
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped
from std_msgs.msg      import Float64
from std_msgs.msg      import Int64
from sensor_msgs.msg       import Joy
from std_msgs.msg import String

class return_using_Autoware():
    def __init__(self):
	self.sub_CNN_flag=0
	self.sub_twist_flag=0
	self.sub_distance_flag=0
	self.distance_flame = 0

        self._sub = rospy.Subscriber('/joy/CNN/cmd_vel', Twist, self.callback_CNN)
        self._sub1 = rospy.Subscriber('/twist_cmd', TwistStamped, self.callback_twist)
        self._sub2 = rospy.Subscriber('/cyclops_distance_to_next_waypoint', Float64, self.callback_distance)
        self._sub3 = rospy.Subscriber('/joy',Joy,self.callback_joy)

        self._pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self._pub1 = rospy.Publisher('/distance_flame', Int64, queue_size=1)
        self._pub2 = rospy.Publisher('/publish_singnal_type', String, queue_size=1)

    def callback(self):

       if(self.sub_CNN_flag==1 and self.sub_twist_flag==1 and self.sub_distance_flag==1):

            self.sub_CNN_flag=0
            self.sub_twist_flag=0
            self.sub_distance_flag=0

            twist = Twist()

            if (self.joy_msg0.buttons[4]==0 and self.joy_msg0.buttons[5]==0):
                 ac = self.twist_msg0.twist.linear.x

                 if(self.distance_flame == 0 ):
                     stre = self.CNN_msg0.angular.z * ac
                     pubtype = "Cyclops"

                 else:
                     stre = self.twist_msg0.twist.angular.z
                     self.distance_flame = self.distance_flame-1
                     pubtype = "Autoware"

            if(self.joy_msg0.buttons[4]==1 and self.joy_msg0.buttons[5]==0):
                 ac = self.twist_msg0.twist.linear.x
                 stre = self.twist_msg0.twist.angular.z
                 pubtype = "Autoware"

            if(self.joy_msg0.buttons[4]==0 and self.joy_msg0.buttons[5]==1):
                 ac = self.CNN_msg0.linear.x
                 stre = self.CNN_msg0.angular.z
                 pubtype = "Cyclops"

            if(self.joy_msg0.buttons[4]==1 and self.joy_msg0.buttons[5]==1):
                 ac = self.joy_msg0.axes[0]
                 stre = self.joy_msg0.axes[3]
                 pubtype = "Joy"

            twist.linear.x = ac
            twist.angular.z = stre
            self._pub.publish(twist)
            self._pub1.publish(self.distance_flame)
            self._pub2.publish(pubtype)

	    print pubtype


    def callback_CNN(self,CNN_msg):
	    self.sub_CNN_flag=1
	    self.CNN_msg0 = CNN_msg
	    self.callback()

    def callback_twist(self,twist_msg):
	    self.sub_twist_flag=1
	    self.twist_msg0 = twist_msg
	    self.callback()

    def callback_distance(self,distance_msg):
	    self.sub_distance_flag=1
	    self.distance_msg0 = distance_msg
            if(self.distance_msg0.data > 0.3):
               self.distance_flame = 100
	    self.callback()


    def callback_joy(self,joy_msg):
	    self.joy_msg0 = joy_msg

            #print(joy_msg.axes[0])#left stic left right
            #print(joy_msg.axes[1])#left stic high low
            #print(joy_msg.axes[2])#right stic left right
            #print(joy_msg.axes[3])#right stic high low
            #print(joy_msg.buttons[4])#left L buttons
            #print(joy_msg.buttons[5])#right R buttons

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('return_using_Autoware')
    tensor = return_using_Autoware()
    tensor.main()


