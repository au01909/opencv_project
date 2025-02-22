import cv2
import numpy as np

# Function to highlight red color and make other areas grayscale
def highlight_and_gray(frame, lower_red1, upper_red1, lower_red2, upper_red2):
    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks for detecting red in two different HSV ranges
    red_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)  # First red range
    red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)  # Second red range

    # Combine both red masks into one
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    # Extract the red-colored areas from the original image
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Convert the entire frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Create an inverse mask to select non-red areas
    inverse_red_mask = cv2.bitwise_not(red_mask)
    
    # Apply the inverse mask to keep non-red areas in grayscale
    gray_result = cv2.bitwise_and(gray_frame, gray_frame, mask=inverse_red_mask)
    gray_result = cv2.cvtColor(gray_result, cv2.COLOR_GRAY2BGR)  # Convert back to 3 channels

    # Merge the highlighted red parts with the grayscale background
    final_result = cv2.add(red_result, gray_result)

    return final_result

# Main function to capture video and apply the effect
def main():
    # Open the default camera (usually camera index 0)
    cap = cv2.VideoCapture(0)

    # Define the red color range in HSV (both lower and upper ranges)
    lower_red1 = np.array([0, 50, 50])   # Lower red range
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])  # Upper red range
    upper_red2 = np.array([180, 255, 255])

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break  # Exit if no frame is captured

        # Optional: Flip the frame horizontally to correct mirror effect
        frame = cv2.flip(frame, 1)

        # Apply red highlighting with grayscale background
        result = highlight_and_gray(frame, lower_red1, upper_red1, lower_red2, upper_red2)

        # Display the original and processed frames
        cv2.imshow('Original', frame)
        cv2.imshow('Highlighted Red and Grayscale', result)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
