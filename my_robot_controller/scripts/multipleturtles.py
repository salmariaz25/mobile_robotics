#!/usr/bin/env python3

import rospy
from turtlesim.srv import Spawn, SpawnRequest
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def spawnttl(name, x, y, theta):
    try:
        spawnproxy = rospy.ServiceProxy('/spawn', Spawn)
        #this line helps is calling a ros service. Helps to interact with ros services

        spawnreq = SpawnRequest()
        #this is a message type which is specific in spawn service.
        #this is what packages the parameteres to spawn the turtles accurately 

        spawnreq.name = name
        #sets the name of the turtle

        spawnreq.x = x
        #sets the x cordinate of the turtles position

        spawnreq.y = y
        #sets the y cordinate of the turtles position

        spawnreq.theta = theta
        #sets the angle value of the turtles position

        spawnproxy(spawnreq)
        #the service call to spawn the turtle takes place

    except rospy.ServiceException as e:
        print(f"Service call failed: {e}")
        #incase of error in the try block, except block is executed and printed

def moveturtle(turtlename, dx):
#defines the moveturtle function which takes two parameters

    movecmd = Twist()
    #created a new twist message object
    
    if dx > 10.0:
        movecmd.linear.x = 0.8
        movecmd.angular.z = 1.2
        #if the x value of turtle is more than 10.0 then turn 1.2 in angular z and go straight in linear x

    elif dx < 1.0:
        movecmd.linear.x = 0.8
        movecmd.angular.z = -1.2
        #if the x value of turtle is less than 1.0 then turn 1.2 in angular z and go straight in linear x

    else:
        movecmd.linear.x = 1.5
        movecmd.angular.z = 0.0
        #or else go straight in linear x

    if turtlename == 'turtle1':
        rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10).publish(movecmd)
    elif turtlename == 'my_turtle1':
        rospy.Publisher('/my_turtle1/cmd_vel', Twist, queue_size=10).publish(movecmd)
    elif turtlename == 'my_turtle2':
        rospy.Publisher('/my_turtle2/cmd_vel', Twist, queue_size=10).publish(movecmd)
    #checks the value of turtlename and publishes the velocity to the respective topics  

def callback(data, turtlename):
#callback function is called whenever the turtles pose updates
#defines the callback function which takes two parameters

    dx = data.x
    #extracts the x-cordinate from the recieved data of the subscribed pose topic

    moveturtle(turtlename, dx)
    #calls the moveturtle function with 2 arguments
    #the turtlename in this allows the function to know which turtle the callback is handling

def multivacturtles():
#defines the multivacturtles function

    rospy.init_node('multiturtles', anonymous=True)
    #initializing the node named as multiturtles
    
    turtle0name = 'turtle1'
    turtle1name = 'my_turtle1'
    turtle2name = 'my_turtle2'
    #assigning each turtle to a variable to name it

    spawnttl(turtle1name, 1.0, 1.0, 0.0)
    spawnttl(turtle2name, 3.0, 3.0, 0.0)
    # Spawning each turtles along with its name, x, y and theta cordinates

    rospy.Subscriber('/turtle1/pose', Pose, callback, turtle0name)
    rospy.Subscriber('/my_turtle1/pose', Pose, callback, turtle1name)
    rospy.Subscriber('/my_turtle2/pose', Pose, callback, turtle2name)
    # Subscribing to the pose topic for each turtles along with its name, type, callback and its argument

    rospy.spin()
    #keeps the python script running as well as handles ROS events.

if __name__ == '__main__':
#checks if the python script is run as the main program
    try:
        multivacturtles()
        #calls the multivacturtles function which contains the main logic of the program

    except rospy.ROSInterruptException:
        pass

