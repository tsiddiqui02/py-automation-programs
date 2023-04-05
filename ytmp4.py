from pytube import YouTube
import os
  
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
  
# extract audio
video = yt.streams.filter(only_video=True).first()
  
# download the file in current directory
destination = os.curdir
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)
print(yt.title + " has been successfully downloaded.")