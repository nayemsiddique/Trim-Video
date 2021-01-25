from moviepy.editor import *
vid= VideoFileClip('./video.mp4')

startTime=0.0
endTime= 3*60

output= vid.subclip(startTime,endTime)

output.write_videofile('./out.mp4',codec='libx264')

