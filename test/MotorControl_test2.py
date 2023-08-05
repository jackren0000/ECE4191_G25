######### This is the motor control test using gpiozero.Robot library

from gpiozero import Robot
from time import sleep

# Initialize the robot
robot = Robot(left = (4, 14), right = (17, 18))

# Move forward
print('Moving forward')
robot.forward()
sleep(2) # Move for 2s

# Move backward
print('Moving backward')
robot.backward()
sleep(2) # Move for 2s

# Turn right
print('Turning right')
robot.right()
sleep(2) # Turn for 2s

# Turn left
print('Turning left')
robot.left()
sleep(2)

# Stop
print('Stopping')
robot.stop()
