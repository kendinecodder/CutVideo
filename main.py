from moviepy.editor import *

videom = VideoFileClip("Kurbağa.mp4")
a = videom.subclip(t_start=2) # The int value represents start time in seconds
a.write_videofile("denedim.mp4")



