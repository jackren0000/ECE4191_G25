import cv2
from pyzbar.pyzbar import decode

class Robot:
    def __init__(self, x, y, cap):
        self.x = x
        self.y = y
        self.cap = cap
        self.target_area = 100

    def navigate_to(self):
        qr_area = 0
        while qr_area < self.target_area:
            # Capture a frame from the camera
            _, frame = self.cap.read()

            # Decode QR codes from the frame
            codes = decode(frame)

            # If no codes are detected, raise an error
            if not codes:
                raise ValueError("No QR code detected")
            
            # Otherwise, take the detected QR code
            code = codes[0]

            # Calculate the center of the QR code and its area
            left, top, width, height = code.rect
            qr_center_x = left + width / 2
            qr_center_y = top + height / 2
            qr_area = width * height

            if self.x < qr_center_x:
                self.x += 1
            elif self.x > qr_center_x:
                self.x -= 1

            if self.y < qr_center_y:
                self.y += 1
            elif self.y > qr_center_y:
                self.y -= 1

            print(f"Moved to {self.x}, {self.y}")

# Initialize the camera
cap = cv2.VideoCapture(1)

# Check whether camera is open
if not cap.isOpened():
    raise IOError("Cannot open camera")

# Initialize the robot at (0, 0)
robot = Robot(0, 0, cap)

robot.navigate_to()

# Release the camera for others to use
cap.release()
# Destroy the windows so they won't stay on the screen
cv2.destroyAllWindows()
