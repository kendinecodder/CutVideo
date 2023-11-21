from moviepy.editor import *

videom = VideoFileClip("Kurbağa.mp4")
a = videom.subclip(t_start=2)
a.write_videofile("denedim.mp4")



