from pytube import YouTube
import tkinter
from tkinter import filedialog
from pytube.exceptions import VideoUnavailable
print("Welcome to the lightweight Youtube Video downloader by MrMilitaryMech!")
link = input("Paste in YT link to download: \r\n")
try:
    yt = YouTube(link)
    print("Querying info, please wait...")
    title = yt.title
    stream = yt.streams.get_highest_resolution()
    print("Please select video output folder")
    root = tkinter.Tk()
    root.withdraw()
    outputfolder = filedialog.askdirectory()
    print(f'Dowloading "{title}" to {outputfolder}')
    stream.download(output_path=outputfolder)
    print("Done!")
except VideoUnavailable:
    print("Video is unavailable!")
input("Press enter to exit...")
