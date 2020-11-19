import tkinter
import webbrowser
import youtube_dl
from functools import partial
from youtube_search import YoutubeSearch

win = tkinter.Tk()

searchInp = tkinter.Entry(win)
searchInp.pack()

def playVideo(videoId):
    videoUrl = "https://youtu.be/" + videoId
    ydl_opts = {
        'outtmpl': dir_utils.get_perm_med_dir() + f'/sound_board/{name}.wav',
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([videoUrl])
def search():
    searchQuery = searchInp.get()
    results = YoutubeSearch(searchQuery, max_results=10).to_dict()
    for video in results:
        x = tkinter.Button(win, text=video["title"], command=partial(playVideo, video["id"])).pack()

searchBtn = tkinter.Button(win, command=search, text="Go").pack()

# print(results)

def webOpen(videoId):
    webbrowser.open("https://youtu.be/" + videoId)

win.mainloop()