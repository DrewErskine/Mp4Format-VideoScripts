import moviepy.editor as mpy
import os
print(os.getcwd())


# Set the path to your images
image_folder = './tmp' 
output_video = 'videoGFX.mp4'

# List all png files in the directory and sort them
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.png')])

# Create clips for each image file with a duration based on 24 fps
frame_duration = 1 / 24  # Duration of each frame in seconds
clips = [mpy.ImageClip(image_folder + "/" + image).set_duration(frame_duration) for image in image_files]

# Concatenate clips into a video
video = mpy.concatenate_videoclips(clips, method="compose")
video.write_videofile(output_video, fps=24)  # Set fps to 24
