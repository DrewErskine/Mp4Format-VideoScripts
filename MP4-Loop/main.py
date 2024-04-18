from moviepy.editor import VideoFileClip, concatenate_videoclips

def loop_video(input_path, output_path, loop_count=3):
    # Load the video file
    clip = VideoFileClip(input_path)
    
    # Create a list of the clip repeated
    looped_clip = concatenate_videoclips([clip] * loop_count)
    
    # Write the result to the output file
    looped_clip.write_videofile(output_path, codec="libx264")

# Usage
input_video_path = "videoGFX.mp4"
output_video_path = "output_looped_video.mp4"
loop_video(input_video_path, output_video_path, loop_count=5)
