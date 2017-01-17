#!/usr/bin/env python

import rospy
from Coords import Coords

def talker():
    pub = rospy.Publisher('python_ros_demo_pub', Coords)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    coords = Coords()
    coords.latitude = 59.9740544
    coords.longitude = 11.0448936
    coords.altitude = 113.000

    rospy.loginfo(coords)
    pub.publish(coords)

    while not rospy.is_shutdown():
        rospy.loginfo("%f, %f, %f", coords.latitude, coords.longitude, coords.altitude)
        pub.publish(coords)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
