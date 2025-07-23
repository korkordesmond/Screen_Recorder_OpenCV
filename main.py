import cv2
import numpy as np
import pyautogui
import os

from cv2 import VideoWriter_fourcc


def get_unique_filename(base_name, extension):
    counter = 1
    filename = f"{base_name}{extension}"
    while os.path.exists(filename):
        filename = f"{base_name}({counter}){extension}"
        counter += 1
    return filename

screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)


output_filename = get_unique_filename("screen_recording", ".mp4")

fps = 25.0

fourcc: VideoWriter_fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

recording_duration = (int(input("Enter Duration for the recording(Secs):")))

for _ in range(int(fps * recording_duration)):
    screen = pyautogui.screenshot()

    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    out.write(frame)

out.release()

file_path = os.path.abspath(output_filename)
print(f'File saved as {output_filename} at {file_path}')