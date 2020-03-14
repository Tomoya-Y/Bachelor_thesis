import message_filters
from std_msgs.msg import Int32, Float32

def callback(mode, penalty):
  # The callback processing the pairs of numbers that arrived at approximately the same time

mode_sub = message_filters.Subscriber('mode', Int32)
penalty_sub = message_filters.Subscriber('penalty', Float32)

ts = message_filters.ApproximateTimeSynchronizer([mode_sub, penalty_sub], 10, 0.1, allow_headerless=True)
ts.registerCallback(callback)
rospy.spin()
