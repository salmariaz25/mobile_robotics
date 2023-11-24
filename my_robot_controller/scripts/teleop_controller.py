#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

def teleoperator():

    pubteleop = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    #publishing to the topic cmd_vel

    rospy.init_node('teleopcontrol', anonymous= True)
    #initializing the node named teleopcontrol

    rate = rospy.Rate(1)
    #to control the loops execution rate

    speed = 0.0
    #setting the speed as 0 initially

    print(" Press W to move forward /n Press S to move backwards /n Press A to turn left /n Press D to turn right")
    #printing what each key does to make it easier for the user to use

    speed = float(input("Enter your required speed: "))
    #providing a user the choice to enter the speed they require

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

           

    while not rospy.is_shutdown():
    #as long as rospy is not shutdown
        
        char = move_keys()
        #character read from the keyboard is set to the char variable
        
        teleop_comm = Twist()
        #created a new twist message object

        if char == 'w':
            teleop_comm.linear.x = speed
            #if w is pressed move forward with the speed from user input

        elif char == 'e':
            teleop_comm.linear.x = speed * 2.0
            #if w is pressed move forward with the speed from user input

        elif char == 's':
            teleop_comm.linear.x = -speed
            #if s is pressed move backward with the speed from user input

        elif char == 'a':
            teleop_comm.angular.z = 0.2
            #turns left when a is pressed
        
        elif char == 'd':
            teleop_comm.angular.z = -0.2
            #turns right when d is pressed

        else:
            continue
            #incase any other character other than w,s,a,d is pressed else is executed 

        pubteleop.publish(teleop_comm)
        #the characters retieved from the keyboard which is stored in the teleop_comm variable is published to the cmd_vel topic using the variable pubteleop

        rate.sleep()
        #maintain the loops frequency

if __name__ == '__main__':
#checks if the python script is run as the main program

    try:
        teleoperator()
        #calls the teleoperator function which contains the main logic of the program

    except rospy.ROSInterruptException:
        pass

