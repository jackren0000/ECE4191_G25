# Import Raspeberry Pi GPIO control library
import RPI.GPIO as GPIO
import time

# Define the GPIO pin numbers
PWM1_PIN = 18
PWM2_PIN = 23

# Set up the GPIO pins

# Notice we choose BCM numbering system
GPIO.setmode(GPIO.BCM)
# Set PWM1 and PWM2 as out pins, so they will send the signals
GPIO.setup(PWM1_PIN, GPIO.OUT)
GPIO.setup(PWM2_PIN, GPIO.OUT)

# Set up the PWM frequencies
pwm1 = GPIO.PWM(PWM1_PIN, 100)
pwm2 = GPIO.PWM(PWM2_PIN, 100)

# Function to drive the motor forward
# Speed is duty cycle
def forward(speed):
    pwm1.start(speed)
    pwm2.start(0)

# Funtion to drive the motor backward
def backward(speed):
    pwm1.start(0)
    pwm2.start(speed)

# Function to stop the motor
def stop():
    pwm1.start(0)
    pwm2.start(0)