#!/usr/bin/env python

import rospy
from pub_sub_demo.Pos import Pos

def callback(pos):
  rospy.loginfo("I heard: [x:\t%f\ty:\t%f\tz:\t%f", pos.x, pos.y, pos.z)

def listener():
  rospy.init_node('pos_subscriber_node', anonymous=True)
  
  rospy.Subscriber('pos_publisher', Pos, callback)
  rospy.spin()

if __name__ == '__main__':
    listener()
