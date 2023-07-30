# ECE4191_G25

## QRdetectionAndNavigation.py
This file uses OpenCV to capture image from a camera and Pyzbar to detect QR codes. When the QR code is detected, it moves the 'robot' to these coordinates.

## yolo_QRdetectionAndNavigation.py
This file is similar to the first one but uses YOLO to continuously capture and decode frames from the camera. It calculates the center and area of the QR code in each frame, and moves the robot towards the QR code until the area of the QR code is larger than a predefined target area. The key difference is that in the first file, the destination is pre-defined, but this file uses YOLO to get to the destination without knowing the destination's coordinates.

## QR_generator.py
This file generates QR code images of coordinates.

## MotorControl.py
This file uses the RPI.GPIO library to control two PWM (Pulse Width Modulation) pins on Raspberry Pi 4. Currently, it includes three functions: `forward(speed)`, `backward(speed)`, and `stop()`.

## CheckTheCamera.py
The camera is different on every device. Use this script first to check the camera number.

## InstructionOfConnectingMotor
This is a text file explaining how to connect the motor to a TB9051FTG carrier and Raspberry Pi.

## Ready for improvement
This is a file that needs suggestions and improvements.
