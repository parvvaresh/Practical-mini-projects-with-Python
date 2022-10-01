import moviepy
import moviepy.editor


path_mp4 = "C:\\Users\\Administrator\\Desktop\\My code\\PYTHON\\simple project\\extract mp3 from mp4\mp4\\test.mp4"
video = moviepy.editor.VideoFileClip(path_mp4)

audio = video.audio

path_mp3 = "C:\\Users\\Administrator\\Desktop\\My code\\PYTHON\\simple project\\extract mp3 from mp4\\test.mp3"
audio.write_audiofile(path_mp3)