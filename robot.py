# This file will represent our robot

import numpy as np
import sys, os, time, math

from gpiozero import RotaryEncoder, Robot, OutputDevice, PWMOutputDevice

class CustomRobot:
    def __init__(self, **kwargs):
        # Not running on remote machine, don't need ssh info -> Caveat might be CV, check with team

        # Do we need to define pins or hardcode? Defining prob better if we need to change :P
        self.left_motor_pins = kwargs['left_motor_pins'] # PWM out
        self.right_motor_pins = kwargs['right_motor_pins'] # PWM out

        self.left_encoder_pins = kwargs['left_encoder_pints'] # Input to PI
        self.right_encoder_pins = kwargs['right_encoder_pins'] # Input to PI

        self.left_encoder = RotaryEncoder(self.left_encoder_pins, max_steps=1000000)
        self.right_encoder = RotaryEncoder(self.right_encoder_pins, max_steps=1000000)

        # Motor
            # Set velocity (PWM)
                # Forward
                # Rotational
            # Receive feedback (odom)

        # Ultrasonic Sensor
            # Send trigger
            # Receive distance

        # Camera
            # Send trigger
            # Receive image
            # Process?

        # Model Params
            # Calibration

        self.robot = Robot(left=self.left_motor_pins, right=self.right_motor_pins, pwm=True)

    def set_velocity(self, velocity=[0,0], duration=None): 
        '''
        Function to set Robot's velocity.

        Inputs:
        - velocity: List, first element is forward velocity and second element is rotational velocity
        - time: Time in seconds to apply velocity
        '''
        start_time = time.time()
        while (time.time() - start_time) < duration:
            # Driving Forward
            if velocity[0] > 0 and velocity[1] == 0: # Forward
                self.left_motor_pins[0].start(velocity[0]) # [0] is PWM1, [1] is PWM2
                self.right_motor_pins[0].start(velocity[0])
                self.left_motor_pins[1].start(0)
                self.right_motor_pins[1].start(0)
            elif velocity[0] < 0 and velocity[1] == 0: # Backwards
                self.left_motor_pins[0].start(0) # [0] is PWM1, [1] is PWM2
                self.right_motor_pins[0].start(0)
                self.left_motor_pins[1].start(velocity[0])
                self.right_motor_pins[1].start(velocity[0])
            elif velocity[0] == 0 and velocity[1] > 0: # Right
                self.left_motor_pins[0].start(velocity[1]) # [0] is PWM1, [1] is PWM2
                self.right_motor_pins[0].start(0)
                self.left_motor_pins[1].start(0)
                self.right_motor_pins[1].start(velocity[1])
            elif velocity[0] == 0 and velocity[1] < 0: # Left
                self.left_motor_pins[0].start(0) # [0] is PWM1, [1] is PWM2
                self.right_motor_pins[0].start(velocity[1])
                self.left_motor_pins[1].start(velocity[1])
                self.right_motor_pins[1].start(0)
        
        # Stop
        self.left_motor_pins[0].start(0) # [0] is PWM1, [1] is PWM2
        self.right_motor_pins[0].start(0)
        self.left_motor_pins[1].start(0)
        self.right_motor_pins[1].start(0)






