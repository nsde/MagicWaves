import tkinter
import webbrowser
from functools import partial
from youtube_search import YoutubeSearch

win = tkinter.Tk()

def search():
    results = YoutubeSearch("legends never die lol", max_results=10).to_dict()
    for video in results:
        print(video["id"])
        x = tkinter.Button(win, text=video["title"], command=partial(webOpen, video["id"])).pack()

searchInp = tkinter.Entry(win).pack()
searchBtn = tkinter.Button(win, command=search).pack()

# print(results)

def webOpen(videoId):
    webbrowser.open("https://youtu.be/" + videoId)

win.mainloop()