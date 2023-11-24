#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def vacuum():
    rospy.init_node('myvacuumturtle', anonymous = True)
    #initializing the node named mmyvacuumturtle

    pubvac = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    #publishing to the topic cmd_vel

    rate = rospy.Rate(1)
    #to control the loops execution rate

    dx = 0
    dy = 0
    #setting x and y values as 0 initially


    def callback(data):
        #callback function is called whenever the turtles pose updates
        #updating the nonlocal variables x and y with the data recieved from the topic pose
        nonlocal dx, dy
        dx = data.x
        dy = data.y

    subvac = rospy.Subscriber('/turtle1/pose', Pose, callback)
    #subscribing to the topic pose 


    while not rospy.is_shutdown():
        #as long as rospy is not shutdown

        movecmd =  Twist()
        #created a new twist message object

        if (dx > 10.0): 
                movecmd.linear.x = 0.8
                movecmd.angular.z = 1.2
                #if the x value of turtle is more than 9.5 then turn 1.2 in angular z and go straight in linear x
            

        elif (dx < 1.0):
                movecmd.linear.x = 0.8
                movecmd.angular.z = -1.2
                #if the x value of turtle is less than 1.5 then turn 1.2 in angular z and go straight in linear x

        else:
                movecmd.linear.x = 1.5
                movecmd.angular.z = 0.0
                #or else go straight in linear x

        pubvac.publish(movecmd)
        #publish to the cmd_vel topic via the pubdet variable


if __name__ == '__main__':
#checks if the python script is run as the main program
    try:
        vacuum()
        #calls the vacuum function which contains the main logic of the program

    except rospy.ROSInterruptException:
        pass
