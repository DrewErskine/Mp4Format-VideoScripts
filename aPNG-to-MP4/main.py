import moviepy.editor as mpy
import os
import logging

# logging - Cool user ui for the progress
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_video_from_images(image_folder, output_video):
    logging.info(f"Current working directory: {os.getcwd()}")

    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.png')])
    frame_duration = 1 / 24  # Duration of each frame in seconds
    clips = [mpy.ImageClip(os.path.join(image_folder, image)).set_duration(frame_duration) for image in image_files]

    video = mpy.concatenate_videoclips(clips, method="compose")
    video.write_videofile(output_video, fps=24)
    logging.info(f"Video file created successfully: {output_video}")

# Usage
image_folder = './tmp'
output_video = 'videoGFX.mp4'
create_video_from_images(image_folder, output_video)
