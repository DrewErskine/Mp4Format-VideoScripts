from moviepy.editor import VideoFileClip, concatenate_videoclips
import logging

# logging - Cool user UI for the progress
logging.basicConfig(level=logging.INFO)

def loop_video(input_path, output_path, loop_count):
    # Load the video
    clip = VideoFileClip(input_path)
    
    # Clip is repeated
    looped_clip = concatenate_videoclips([clip] * loop_count)
    
    # Output file
    looped_clip.write_videofile(output_path, codec="libx264")
    logging.info(f"The video looped {loop_count} times. Output = {output_path}")

    clip.close()
    looped_clip.close()

input_video_path = "videoGFX.mp4"
output_video_path = "output_looped_video.mp4"

# Get user input for loop count
try:
    user_input = int(input("Enter the number of times you want the video to loop: "))
    loop_video(input_video_path, output_video_path, loop_count=user_input)
except ValueError:
    logging.error("Please enter a number for the number of times looped.")
