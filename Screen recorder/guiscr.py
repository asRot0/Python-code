import tkinter as tk
import threading
import cv2
import numpy as np
import pyautogui

class ScreenRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")

        self.recording = False
        self.resolution = (1920, 1080)
        self.filename = "Recording.avi"
        self.codec = cv2.VideoWriter_fourcc(*"XVID")
        self.fps = tk.StringVar(value="60")  # Default FPS value

        # FPS dropdown list
        fps_label = tk.Label(self.root, text="Select FPS:")
        fps_label.pack()

        fps_options = ["10", "15", "20", "24", "30", "60"]
        fps_dropdown = tk.OptionMenu(self.root, self.fps, *fps_options)
        fps_dropdown.pack()

        self.record_button = tk.Button(root, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack()

        # Create a canvas for smoother live video display
        self.live_canvas = tk.Canvas(self.root, width=480, height=270)
        self.live_canvas.pack()

    def start_recording(self):
        self.recording = True
        self.fpsvalue = int(self.fps.get())
        self.out = cv2.VideoWriter(self.filename, self.codec, self.fpsvalue, self.resolution)

        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)

            # Display the recording on the canvas
            frame = cv2.resize(frame, (480, 270))
            img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.imencode('.png', img)[1].tobytes()
            self.display_image(img)

        self.out.release()

    def stop_recording(self):
        self.recording = False

    def toggle_recording(self):
        if not self.recording:
            self.record_button.config(text="Stop Recording")
            recording_thread = threading.Thread(target=self.start_recording)
            recording_thread.start()
        else:
            self.record_button.config(text="Start Recording")
            self.stop_recording()

    def display_image(self, image_data):
        image = tk.PhotoImage(data=image_data)
        self.live_canvas.create_image(0, 0, anchor="nw", image=image)
        self.live_canvas.image = image

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()
