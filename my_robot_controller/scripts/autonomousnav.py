#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class autonomous:
    def __init__(self):
        rospy.init_node('autonav', anonymous=True)
        #initializing the node naming it autonav

        self.navpub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        #publishing to the topic cmd_vel
        
        self.navsub = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        #subscribing to the topic pose 

        self.pose = Pose()
        #initialize current pose to know where the turtles position is at currently

        self.rate = rospy.Rate(10)

    def callback(self, data):
        #callback function is called whenever the turtles pose updates

        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def navigate(self, nav_x, nav_y):
       
        dist =  sqrt(pow((nav_x - self.pose.x), 2) + pow((nav_y - self.pose.y), 2))
        #calculating the distance to the coordinates recieved from the user

        linear_vel = 1.5 * dist
        #calculating the linear velocity to the mentioned cordinates

        angle = atan2(nav_y - self.pose.y, nav_x - self.pose.x)
        #calculate the angle to turn in order to approach the given coordinates

        angular_vel = 4.0 * (angle - self.pose.theta)
        #calculating the angular velocity proportional to the angle

        vel_msg = Twist()
        #created a new twist message object

        vel_msg.linear.x = linear_vel
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        vel_msg.angular.z = angular_vel
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        #asigning the calculated velocity values to linear and angular to publish to the cmd_vel topic
        #setting the remaining as 0

        self.navpub.publish(vel_msg)
        #publish to the cmd_vel topic via the navpub variable


        self.rate.sleep()

        

if __name__ == '__main__':
    try:
        auto_navigation = autonomous()

        # Prompt the user to enter target coordinates
        nav_x = float(input('Enter your x coordinate: '))
        nav_y = float(input('Enter your y coordinate: '))

        auto_navigation.navigate(nav_x, nav_y)

    except rospy.ROSInterruptException:
        pass
