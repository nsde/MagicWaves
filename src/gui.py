import tkinter
import webbrowser
import youtube_dl

from pathlib import Path
from functools import partial
from youtube_search import YoutubeSearch

win = tkinter.Tk()
win.title('MagicWaves')
win.config(bg='#151515')
win.geometry('400x400')

search_frame = tkinter.Frame(win, bg='#2E2E2E')
search_frame.pack()

search_input = tkinter.Entry(search_frame, font=('Yu Gothic', 20), fg='white', bg='#2E2E2E', relief='flat')
search_input.pack(side='left')
search_input.focus_set() 

def playVideo(video_id, video_name):
    video_url = 'https://youtu.be/' + video_id
    ydl_opts = {
        'outtmpl': str(Path.home()) + f'/sound_board/{video_name}.wav',
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def search():
    max_results = 10

    # delete all previous search results (if any)
    try:
        for _ in range(max_results):
            result_title = result_num
    except:
        pass

    # handle search input
    search_query = search_input.get()
    print(f'Searching \'{search_query}\'...')
    results = YoutubeSearch(search_query, max_results=max_results).to_dict()

    result_frame = tkinter.Frame(win, bg='#2E2E2E')
    result_frame.pack()

    # display results
    result_num = 0
    for video in results:
        result_num += 1

        print(video)
        
        exec(f'result_title{result_num} = tkinter.Button(win, font=(\'Yu Gothic\', 10), fg=\'white\', bg=\'#2E2E2E\', relief=\'flat\', text=video[\'title\'], command=partial(playVideo, video_id=video[\'id\'], video_name=video[\'title\']))')
        exec(f'result_title{result_num}.pack()')

search_button = tkinter.Button(search_frame, command=search, text='>', font=('Yu Gothic', 20), fg='white', bg='#2E2E2E', relief='flat')
search_button.pack(side='right')

# print(results)

def webOpen(video_id):
    webbrowser.open('https://youtu.be/' + video_id)

win.mainloop()