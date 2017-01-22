#!/usr/bin/env python

import rospy
from pub_sub_demo.Pos import Pos

def talker():
    pub = rospy.Publisher('pos_publisher', Pos)
    rospy.init_node('pos_publisher_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    pos = Pos()
    pos.x = 1
    pos.y = 2
    pos.z = 3

    while not rospy.is_shutdown():
        rospy.loginfo("Sending: [x:\t%f\ty:\t%f\tz:\t%f", pos.x, pos.y, pos.z)
        pub.publish(pos)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
