import RPi.GPIO as GPIO
import time

PWM = 17 # replace with your actual pin number

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWM, GPIO.OUT)

# Create PWM object
p = GPIO.PWM(PWM, 100)  # 100Hz frequency

while (True):
  p.start(90)  # Start with 50% duty cycle
  time.sleep(2)  # run for 2 seconds
  p.stop()  # Stop PWM
  time.sleep(2) # stop for 2 seconds
