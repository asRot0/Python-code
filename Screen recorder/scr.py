import pyautogui
import cv2
import numpy as np

# Screen resolution
screen_width, screen_height = pyautogui.size()

# Set the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (screen_width, screen_height))

while True:
    # Capture the screen
    img = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array
    frame = np.array(img)

    # BGR -> RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) == ord("q"):
        break

out.release()
cv2.destroyAllWindows()
