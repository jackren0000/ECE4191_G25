# ECE4191_G25


1. QRdetectionAndNavigation.py:
The file uses OpenCV to capture image from a camera and Pyzbar to detect QR codes,
when the QR code is detected, it moves the 'robot' to these coordinates.

2. yolo_QRdetectionAndNavigation.py
This file is like the first one but uses YOLO to continuously capture and decode frames from the camera, calculates the center and area of the QR code in each frame, and moves the robot towards the QR code until the area of the QR code is larger than a predefined target area.
The key difference is in the file the destination is pre-defined, but this file using YOLO to get to the destination without knowing the destinations coordinates.

4. QR_generator.py:
This file generate QR code image of coordinates.

5. MotorControl.py:
This file is using the RPI.GPIO library to control two PWM (Pulse Width Modulation) pins on Raspberry Pi 4.
There are 3 functions right now: forward(speed), backward(speed), and stop().

6. CheckTheCamera.py:
The camera is different in every device, using this scipt first to check the camera number.

7. InstructionOfConnectingMotor
This is a text file of how to connect the motor to TB9051FTG carrier and Raspberry pi.

8. Ready for improvement
This is the file needs suggestion and improvement.
