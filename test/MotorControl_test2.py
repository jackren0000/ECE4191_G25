import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define your motor control pins
EN = 22  
ENB = 23  
PWM1 = 17 
PWM2 = 27 

# Set up the motor control pins
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(PWM1, GPIO.OUT)
GPIO.setup(PWM2, GPIO.OUT)

p = GPIO.PWM(EN, 100)  # 100Hz frequency

try:
    while True:
        # Start the motor in forward/coast mode at 50% speed
        GPIO.output(PWM1, GPIO.HIGH)
        GPIO.output(PWM2, GPIO.LOW)
        p.start(50)

        time.sleep(2)  # run for 2 seconds

        # Change direction to reverse/coast at 75% speed
        GPIO.output(PWM1, GPIO.LOW)
        GPIO.output(PWM2, GPIO.HIGH)
        p.ChangeDutyCycle(75)

        time.sleep(2)  # run for 2 seconds

except KeyboardInterrupt:
    # Stop the motor and clean up GPIO state
    p.stop()
    GPIO.cleanup()
