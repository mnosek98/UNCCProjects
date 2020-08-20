#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt32



def callbackA(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
def callbackB(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
	rospy.init_node('node_c')
	rospy.Subscriber("topic_a", String, callbackA)
	rospy.Subscriber("topic_b", UInt32, callbackB)
	rospy.spin()


if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass
