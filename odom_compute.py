#!/usr/bin/env python
import rospy
import math
import tf.transformations
from turtlebot3_msgs.msg import SensorState
from nav_msgs.msg import Odometry


def callback(data):
	
	#left_encoder = data.lwheel
	#right_encoder = data.rwheel
	

def talker():
	rospy.init_node('odom_compute', anonymous=True)
	rospy.Subscriber("sensor_state", SensorState, callback)
	#print left_encoder
	#print right_encoder
	print data.lwheel
	rate = rospy.Rate(10) # 10hz
	
	

if __name__ == '__main__':
	talker()

