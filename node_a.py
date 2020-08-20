#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt32


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def talker():
	pub = rospy.Publisher('topic_a', String, queue_size=10)
	rospy.init_node('node_a', anonymous=True)
	rospy.Subscriber("topic_b", UInt32, callback)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
