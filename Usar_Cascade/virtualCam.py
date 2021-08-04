import pyvirtualcam
import numpy as np

with pyvirtualcam.Camera(width=1366, height=768, fps=30) as cam:
    while True:
        frame = np.zeros((cam.height, cam.width, 4), np.uint8) # RGBA
        frame[:,:,:3] = cam.frames_sent % 255 # grayscale animation
        frame[:,:,3] = 255
        cam.send(frame)
        cam.sleep_until_next_frame()
        cam.sleep_until_next_frame()