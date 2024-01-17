import cv2
import numpy as np

def highlight_and_gray(frame, color_lower, color_upper):
    # Convert the frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define a mask using the specified color range for red
    red_mask = cv2.inRange(hsv, color_lower, color_upper)

    # Apply the red mask to the original frame
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert areas outside the red range to grayscale
    inverse_red_mask = cv2.bitwise_not(red_mask)
    gray_result = cv2.bitwise_and(gray_frame, gray_frame, mask=inverse_red_mask)

    # Combine the highlighted red and grayscale results
    final_result = cv2.add(red_result, cv2.cvtColor(gray_result, cv2.COLOR_GRAY2BGR))

    return final_result

def main():
    # Open the default camera (usually camera index 0)
    cap = cv2.VideoCapture(0)

    # Define the lower and upper bounds of the red color in HSV
    red_lower = np.array([0, 50, 50])
    red_upper = np.array([10, 255, 255])

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is successfully read
        if not ret:
            break

        # Highlight red and convert other colors to grayscale
        result = highlight_and_gray(frame, red_lower, red_upper)

        # Display the original and processed frames
        cv2.imshow('Original', frame)
        cv2.imshow('Highlighted Red and Grayscale', result)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
