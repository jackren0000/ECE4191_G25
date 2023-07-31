# Import Raspeberry Pi GPIO control library
import RPI.GPIO as GPIO
import time

# Define the GPIO pin numbers for the two motors
MOTOR1_PWM1_PIN = 18
MOTOR1_PWM2_PIN = 23
MOTOR2_PWM1_PIN = 24
MOTOR2_PWM2_PIN = 25

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM) # Notice we choose BCM numbering system
# Set PWM1 and PWM2 as out pins, so they will send the signals
GPIO.setup(MOTOR1_PWM1_PIN, GPIO.OUT)
GPIO.setup(MOTOR1_PWM2_PIN, GPIO.OUT)
GPIO.setup(MOTOR2_PWM1_PIN, GPIO.OUT)
GPIO.setup(MOTOR2_PWM2_PIN, GPIO.OUT)

# Set up the PWM frequencies
motor1_pwm1 = GPIO.PWM(MOTOR1_PWM1_PIN, 100)
motor1_pwm2 = GPIO.PWM(MOTOR1_PWM2_PIN, 100)
motor2_pwm1 = GPIO.PWM(MOTOR2_PWM1_PIN, 100)
motor2_pwm2 = GPIO.PWM(MOTOR2_PWM2_PIN, 100)

# Function to drive the robot forward
def forward(speed):
    motor1_pwm1.start(speed)
    motor1_pwm2.start(0)
    motor2_pwm1.start(speed)
    motor2_pwm2.start(0)

# Function to turn the robot left
def left(speed):
    motor1_pwm1.start(0)
    motor1_pwm2.start(speed)
    motor2_pwm1.start(speed)
    motor2_pwm2.start(0)

# Function to turn the robot right
def right(speed):
    motor1_pwm1.start(speed)
    motor1_pwm2.start(0)
    motor2_pwm1.start(0)
    motor2_pwm2.start(speed)

# Function to stop the robot
def stop():
    motor1_pwm1.start(0)
    motor1_pwm2.start(0)
    motor2_pwm1.start(0)
    motor2_pwm2.start(0)
