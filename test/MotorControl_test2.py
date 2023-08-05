######### This is the motor control test using gpiozero.Robot library

from gpiozero import Motor
from time import sleep

# Initialize the motor
motor = Motor(forward=17, backward=27)

# Spin in one direction
motor.forward()
sleep(2)

# Spin in the other direction
motor.backward()
sleep(2)

# Stop the motor
motor.stop()
