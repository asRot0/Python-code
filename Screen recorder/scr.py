import tkinter as tk
import threading
import cv2
import numpy as np
import pyautogui
from tkinter import ttk

class ScreenRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")

        self.recording = False
        self.resolution = (1920, 1080)
        self.filename = "Recording.avi"
        self.codec = cv2.VideoWriter_fourcc(*"XVID")
        self.fps = 30  # Default FPS value

        # Create and configure the GUI elements
        self.create_gui()

    def create_gui(self):
        # FPS Label and Dropdown
        fps_label = tk.Label(self.root, text="Select FPS:")
        fps_label.pack()

        fps_options = ["10", "15", "20", "24", "30", "60"]
        self.fps_var = tk.StringVar()
        self.fps_var.set("30")  # Default FPS
        fps_dropdown = ttk.Combobox(self.root, textvariable=self.fps_var, values=fps_options)
        fps_dropdown.pack()

        # Start/Stop Button
        self.record_button = tk.Button(self.root, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack()

        # Live Video Frame
        self.live_frame = tk.Label(self.root)
        self.live_frame.pack()

    def start_recording(self):
        self.recording = True
        self.fps = int(self.fps_var.get())
        self.out = cv2.VideoWriter(self.filename, self.codec, self.fps, self.resolution)

        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)

            # Display the recording on the GUI
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame = cv2.resize(frame, (480, 270))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())
            self.live_frame.img = img
            self.live_frame.config(image=img)
            self.live_frame.update()

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

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()
