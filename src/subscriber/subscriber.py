#!/usr/bin/env python

import rospy
from Coords import Coords

def callback(coords):
  rospy.loginfo("Received: %f, %f, %f", coords.latitude, coords.longitude, coords.altitude)

def listener():
  rospy.init_node('subscriber', anonymous=True)
  
  rospy.Subscriber('python-ros-demo-pub', Coords, callback)
  rospy.spin()

if __name__ == '__main__':
    listener()
