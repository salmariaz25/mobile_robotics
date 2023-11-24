#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import sys, select, termios, tty



def walldetectorttl():

    rospy.init_node('wall_detector', anonymous = True)
    #initializing the node named wall_detector

    pubdet = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    #publishing to the topic cmd_vel

    rate = rospy.Rate(1)
    #to control the loops execution rate

    x = 0
    y = 0
    #setting x and y values as 0 initially

    def move_keys():

        filedesc = sys.stdin.fileno()
        #retrieving the ID which represents the keyboard

        old_settings = termios.tcgetattr(filedesc)
        #saving the current setting as the old setting to restore it later

        try:
            tty.setraw(filedesc)
            #sets the keyboard as raw so that each keypress is sent directly to the program

            key = sys.stdin.read(1)
            #reads the character from the keyboard

        finally:
            termios.tcsetattr(filedesc, termios.TCSADRAIN, old_settings)
            #restores the orginal keyboard settings

            return key
            #returns the character read from the keyboard

    def callback(data):
        #updating the nonlocal variables x and y with the data recieved from the topic pose
        nonlocal x, y
        x = data.x
        y = data.y

    subdet = rospy.Subscriber('/turtle1/pose', Pose, callback)
    #subscribing to the topic pose 

    
    while not rospy.is_shutdown():
        #as long as rospy is not shutdown
       
        char = move_keys()
        #character read from the keyboard is set to the char variable

        teleop_comm = Twist()
        #created a new twist message object          
            
        if char == 'w':
            teleop_comm.linear.x = 0.5
            #when character w is pressed move forward
            if x > 10 or x < 1.5 or y > 10 or y < 1.5:
                teleop_comm.linear.x = 0.0
                print("Alert! Not allowed any further as turtle will crash!")
                #when the turtle approaches above 10 in x and y axis as well as below 1.5 in the same print the alert message
            else:
                teleop_comm.linear.x = 0.5
                print("The turtle is safe")
                #if the turtle is anywhere else print the safe message
                
        elif char == 's':
            teleop_comm.linear.x = -0.5
            #when character s is pressed move backward
            if x > 10 or x < 1.5 or y > 10 or y < 1.5:
                teleop_comm.linear.x = 0.0    
                print("Alert! Not allowed any further as turtle will crash!")
                #when the turtle approaches above 10 in x and y axis as well as below 1.5 in the same print the alert message
            else:
                teleop_comm.linear.x = -0.5
                print("The turtle is safe")
                #if the turtle is anywhere else print the safe message

        elif char == 'a':
            teleop_comm.angular.z = 0.2
            #turns left when a is pressed
    
        elif char == 'd':
            teleop_comm.angular.z = -0.2
            #turns right when d is pressed

        else :
            teleop_comm.linear.x = 0.0
            #if no keys are pressed no movements should take place

        pubdet.publish(teleop_comm)
        #publish to the cmd_vel topic via the pubdet variable

        rate.sleep()
        #maintain the loops frequency

    rospy.spin()
    #continues processing incoming messages to keep the program running      
    

if __name__ == '__main__':
#checks if the python script is run as the main program
    try:
        walldetectorttl()
        #calls the walldetectorttl function which contains the main logic of the program

    except rospy.ROSInterruptException:
        pass