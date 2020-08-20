#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
msg = Twist()
current_distance = 0.0
startTime = 0.0
current_theta = 0.0

def callback(data):
	#rospy.loginfo(data)
	print()

def turnTo(theta):
	global current_theta 
	global pub
	global msg
	global startTime 
	rospy.loginfo(startTime)
	if (current_theta < theta):
		pub.publish(msg)
		endTime = rospy.get_rostime().secs
		rospy.loginfo(endTime)
		current_theta= 0.1*(endTime - startTime)
	else:
		msg.angular.x = 0
		msg.angular.y = 0
		msg.angular.z = 0
		msg.linear.x = 0
		msg.linear.y = 0
		msg.linear.z = 0
		pub.publish(msg)

def driveDistance(distance):
	global current_distance 
	global pub
	global msg
	global startTime 
	rospy.loginfo(startTime)
	if (current_distance < distance):
		pub.publish(msg)
		endTime = rospy.get_rostime().secs
		rospy.loginfo(endTime)
		current_distance= 0.2*(endTime - startTime)
	else:
		msg.linear.x = 0
		msg.linear.y = 0
		msg.linear.z = 0
		msg.angular.x = 0
		msg.angular.y = 0
		msg.angular.z = 0
		pub.publish(msg)
	
def move():
	global pub
	global startTime
	rospy.init_node('drive_robot', anonymous = True)
	sub = rospy.Subscriber("/odom", Odometry, callback)
	rate = rospy.Rate(30) # 10hz
	startTime = rospy.get_rostime().secs

	global msg
	msg.linear.x = 0
	msg.linear.y = 0
	msg.linear.z = 0
	msg.angular.x = 0
	msg.angular.y = 0
	msg.angular.z = 0.1
 
	while not rospy.is_shutdown():
		#rospy.loginfo(msg)
		#pub.publish(msg)
		#rospy.sleep(5)
		#rospy.loginfo(current_distance)
		#driveDistance(.8)
		turnTo(3.14)


if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException: pass
