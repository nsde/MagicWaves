import tkinter
import webbrowser
import youtube_dl
from pathlib import Path
from functools import partial
from youtube_search import YoutubeSearch

win = tkinter.Tk()
win.title("MagicWaves")
win.config(bg="#151515")
win.geometry("400x400")

searchInp = tkinter.Entry(win)
searchInp.pack()

def playVideo(videoId, videoName):
    videoUrl = "https://youtu.be/" + videoId
    ydl_opts = {
        'outtmpl': str(Path.home()) + f'/sound_board/{videeoName}.wav',
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([videoUrl])
def search():
    searchQuery = searchInp.get()
    results = YoutubeSearch(searchQuery, max_results=10).to_dict()
    for video in results:
        print(video)
        x = tkinter.Button(win, text=video["title"], command=partial(playVideo, videoId=video["id"]), videoName=video["title"])
        x.pack()

searchBtn = tkinter.Button(win, command=search, text="Go").pack()

# print(results)

def webOpen(videoId):
    webbrowser.open("https://youtu.be/" + videoId)

win.mainloop()