# ECE4191_G25


1. QRdetectionAndNavigation.py:
The file uses OpenCV to capture image from a camera and Pyzbar to detect QR codes,
when the QR code is detected, it moves the 'robot' to these coordinates.

2. QR_generator.py:
This file generate QR code image of coordinates.

3. MotorControl.py:
This file is using the RPI.GPIO library to control two PWM (Pulse Width Modulation) pins on Raspberry Pi 4.
There are 3 functions right now: forward(speed), backward(speed), and stop().

4. CheckTheCamera.py:
The camera is different in every device, using this scipt first to check the camera number.

5.InstructionOfConnectingMotor
This is a text file of how to connect the motor to TB9051FTG carrier and Raspberry pi.
