#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt32

val = 0

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
	global val
	pub = rospy.Publisher('topic_b', UInt32, queue_size=10)
	rospy.init_node('node_b')
	rospy.Subscriber("topic_a", String, callback)
	rate = rospy.Rate(10) # 10hz
	#rospy.spin()
	while not rospy.is_shutdown():	
		val = val + 1
		hello_val = val 
		rospy.loginfo(hello_val)
		pub.publish(hello_val)
		rate.sleep()

if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass
