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

searchFrame = tkinter.Frame(win, bg="#2E2E2E")
searchFrame.pack()

searchInp = tkinter.Entry(searchFrame, font=("Yu Gothic", 20), fg="white", bg="#2E2E2E", relief="flat")
searchInp.pack(side="left")
searchInp.focus_set() 

def playVideo(video_id, video_name):
    videoUrl = "https://youtu.be/" + video_id
    ydl_opts = {
        'outtmpl': str(Path.home()) + f'/sound_board/{video_name}.wav',
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([videoUrl])

def search():
    max_results = 10

    # delete all previous search results (if any)
    try:
        for _ in range(max_results):
            resultTitle + resultNo
    except:
        pass

    # handle search input
    search_query = searchInp.get()
    print(f"Searching '{search_query}'...")
    results = YoutubeSearch(search_query, max_results=max_results).to_dict()

    resultFrame = tkinter.Frame(win, bg="#2E2E2E")
    resultFrame.pack()

    # display results
    resultNo = 0
    for video in results:
        resultNo += 1

        print(video)
        
        exec(f'resultTitle{resultNo} = tkinter.Button(win, font=("Yu Gothic", 10), fg="white", bg="#2E2E2E", relief="flat", text=video["title"], command=partial(playVideo, video_id=video["id"], video_name=video["title"]))')
        exec(f'resultTitle{resultNo}.pack()')

searchBtn = tkinter.Button(searchFrame, command=search, text=">", font=("Yu Gothic", 20), fg="white", bg="#2E2E2E", relief="flat")
searchBtn.pack(side="right")

# print(results)

def webOpen(video_id):
    webbrowser.open("https://youtu.be/" + video_id)

win.mainloop()