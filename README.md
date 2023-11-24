# mobile_robotics

SALMA RIAZ 
M00982503
PDE4430 – CW1
READ ME FILE

teleop_controller.py
The teleop_controller.py is the python file inside the scripts directory which contains the code to move the turtle using the keys ‘w’ , ‘a’ , ‘s’ , ‘d’ .
W – makes the turtle go forward
A – makes the turtle turn left
S – makes the turtle move backwards 
D – makes the turtle turn right 

First run – roscore
Next, open a new terminal and run - rosrun turtlesim turtlesim_node
Then run , rosrun my_robot_controller teleop_controller.py

This file allows the user to choose the speed he wants the turtle to move in, hence the user will first be prompted to enter the speed he requires for the turtle to move. The speed variable is initially set to 0, which is then overwritten once the user enters the required speed. Incase the user wants to increase the speed, he can press the ‘e’ key and move the turtle 2 times faster than the speed he has entered.
The instructions to use the keys for different movements are printed. 
In this program, first the old keyboard settings of the file descriptor is saved by the move_keys() function, this is done so that the original settings can be restored back later.
Then the keyboard setting is set to raw mode, this is done so that each character entered by the user is directly send to the program without the need to press enter.
Single character is read from the keyboard and is stored in the key variable for the program to act upon and finally the original setting of the keyboard it restored back. 
Mainly, the function move_keys() helps in reading the character from the keyboard, stores it in the key variable, allowing the program to react based on the key pressed, which in return controls the movement of the turtle in the turtlesim simulator. Then the If else statement is used for helping in the movement of the turtle. 

walldetecter.py
First run – roscore
Next, open a new terminal and run - rosrun turtlesim turtlesim_node
Then run , rosrun my_robot_controller walldetecter.py
This file similar to the teleop_controller file uses the ‘w’, ‘a’ , ‘s’ , ‘d’ to move the turtle.
Once the turtle moves in the safe zone which is between the values of 1.5 and 10 of the x coordinate then the “the turtle is safe” message will be printed. 
As soon as the turtle hits the wall detector area which is above 10.0 and below 1.5 of the x coordinate then the alert message “Not allowed any further as turtle will crash!” is printed and stops it from going any further.
To help the smooth functioning of this program, if else statements are used. 
If the turtle travels above the mentioned coordinates in the if statement then it is executed. Each is placed within the ‘w’ and ‘s’ key if statements so that once the wall is detected the key no longer works not allowing it to more further.
The turtle travels 0.5 in linear but as soon as the wall is detected with the execution of if statement the value is overwritten and made to 0.0 which makes the turtle stop.
As this is placed within the if else statements of the keys, each time the key is pressed by the user it prints the safe or alert message provided.

Vacuumturtle.py
First run – roscore
Next, open a new terminal and run - rosrun turtlesim turtlesim_node
Then run , rosrun my_robot_controller vacuumturtle.py
In the vacuum file, the program is done in a way where the turtle starts automatically as soon as the python file is run.
The turtle first moves forward from its initial position, the turtle detects that it is approaching above 10.0 in x cordinates hence executes the first if statement which makes it turn according to the mentioned linear and angular values in the if statement, as it is now away from the said coordinate it now executes the else statement which makes it move forward in linear direction. 
Upon detecting the approach of 1.0 in x coordinate the elif statement is executed which makes the turtle now turn around once again moving to the other direction.
This is repeated making it perform like a vacuum cleaning robot.

multipleturtles.py
First run – roscore
Next, open a new terminal and run - rosrun turtlesim turtlesim_node
Then run , rosrun my_robot_controller multipleturtles.py

In the multipleturtles.py file,
Multiple turtles are spawned via the service proxy which helps in calling a ros service. It helps in the interacting with ros services. 
Then the spawnrequest is called which helps in specifying the x, y, theta coordinates as well as the name of the turtle. 
Once the service for spawning is set up, 2 additional turtles are then spawned making it total of 3 turtles on the turtlesim window. 
To make these turtles move in a vacuum cleaning behavior, similar to the previous vacuumturtle.py, if else statements are used and executed making it move forward. 
The turtles detects that they are approaching more than 10.0 in x coordinate making it execute the if statement which turns all three turtles in mentioned values. It then moves forward detects it is approaching less than 1.5 in x cordinate making all three turtles turn again and continue moving forward in opposite linear motion now. This behavior is repeated making all three turtles cover the entire turtlesim window.
All 3 turtles moving simultaneously in a vacuum cleaning behavior can be seen.

Autonomous.py
First run – roscore
Next, open a new terminal and run - rosrun turtlesim turtlesim_node
Then run , rosrun my_robot_controller autonomous.py

In the autonomous.py file,
To approach the x and y coordinates given by the user, first the callback function will retrieve the current position of the turtle in its x and y coordinates. Once it is received it should be rounded to 4 to make the calculation easier. 
Now all the calculations will take place within the navigation function. 
Firstly, the distance between the current position of the turtle and the given coordinate values by the user should be calculated. 
Then the linear velocity to travel the distance should be calculated.
Next, the angle to turn the turtle will be calculated. Which is then used to calculate the angular velocity required to turn this turtle.
Twist message object will be created and the calculated linear velocities will be then later published on the cmd_vel topic.
Upon running the file, the user is prompted to enter the x and y coordinates he wishes.
With the above calculations, the turtle should move to the now calculated position.


