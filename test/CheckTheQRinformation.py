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

            # Print information for all detected QR codes
            for code in codes:
                # Calculate the center of the QR code and its area
                left, top, width, height = code.rect
                qr_center_x = left + width / 2
                qr_center_y = top + height / 2
                qr_area = width * height

                # Print QR code information
                print(f"QR Code Information:")
                print(f"Data: {code.data.decode('utf-8')}")
                print(f"Type: {code.type}")
                print(f"Coordinates: {code.polygon}")
                print(f"Area: {qr_area}")  # Prints the size of the QR code's area

                # Draw rectangle around the QR code
                cv2.rectangle(frame, (left, top), (left + width, top + height), (0, 255, 0), 3)

            # Display the resulting frame
            cv2.imshow('QR Code Detection', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Commented out movement commands
    #           # If QR code's center_x is in the left half of the image, move left
    #           if qr_center_x < frame.shape[1] / 2:
    #               # Replace with actual command to move robot left
    #               print("Moving left")

    #           # If QR code's center_x is in the right half of the image, move right
    #           elif qr_center_x > frame.shape[1] / 2:
    #               # Replace with actual command to move robot right
    #               print("Moving right")

    #           # If QR code's area is smaller than the target area, move forward
    #           if qr_area < self.target_area:
    #               # Replace with actual command to move robot forward
    #               print("Moving forward")
    #           else:
    #               print("Reached the QR code, stopping movement.")
    #               break

# Initialize the camera
cap = cv2.VideoCapture(0)

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
