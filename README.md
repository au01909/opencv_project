# opencv_project
highlighting specific color frame using opencv

# Color Highlighting in Frames

This Python script uses the OpenCV library to capture video frames from a camera and highlight specific colors in the frames while converting other colors to grayscale.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`) library
- NumPy library (`np`)

Install the required libraries using the following:

```bash
pip install opencv-python numpy

Usage
Run the script:
python color_highlight.py

End the Script
Press the 'q' key to exit the application.

Customizing Color Highlighting
You can customize the color to be highlighted by adjusting the lower and upper bounds of the color in the HSV space. Find the HSV values for your desired color and update the color_lower and color_upper values in the script.

Example: Highlighting Red
To highlight red color, you can set the following HSV values:

  # Define the lower and upper bounds of the red color in HSV
    red_lower = np.array([0, 50, 50])
    red_upper = np.array([10, 255, 255])

