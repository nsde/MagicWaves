import magicwaves

import os
import yaml
import time
import tkinter
import urllib.request

from PIL import Image, ImageTk

cwd = os.getcwd()

def gettheme():
    theme = {}
    theme['fg'] = 'white'
    theme['bg'] = '#0E0F13'
    theme['font'] = 'Yu Gothic UI Light'
    theme['title'] = 'Yu Gothic UI Bold'
    theme['light'] = '#008AE6'
    theme['warn'] = '#fc9d19'
    theme['critical'] = '#fc3b19'
    theme['ok'] = '#28ff02'
    return theme

win = tkinter.Tk()
win.title('MagicWaves')
win.config(bg=gettheme()['bg'])
win.geometry('480x500')
win.iconphoto(False, tkinter.PhotoImage(file='media/win.png'))

top_frame = tkinter.Frame(win,
    bg=gettheme()['bg'],
)
top_frame.pack(side='top', anchor='n', ipady=5, fill='x')

title = tkinter.Label(top_frame,
    text='Recommendations',
    font=(gettheme()['title'], 20),
    fg=gettheme()['fg'],
    bg=gettheme()['bg'],
)
title.pack(side='bottom', anchor='w', padx=10)

recommendation_frame = tkinter.Frame(win,
    bg=gettheme()['ok'],
)
recommendation_frame.pack(side='top', anchor='w', padx=10)

tkinter.Label(recommendation_frame,
    text='Video 1',
    font=(gettheme()['font'], 20),
    fg=gettheme()['fg'],
    bg=gettheme()['bg'],
).pack(side='top', anchor='w')

def load_settings():
    return yaml.load(open(cwd + '\\config\\config.yml'), Loader=yaml.FullLoader)

def settings():
    win = tkinter.Tk()
    win.title('MagicWaves - Settings')
    win.config(bg=gettheme()['bg'])
    win.geometry('400x400')

    config = load_settings()
    print('Configtype' + str(type(config['performance']['video_thumbnails'])))

    win.mainloop()

tkinter.Button(top_frame,
    text='⚙️',
    command=settings,
    font=(gettheme()['font'], 20),
    fg=gettheme()['fg'],
    height=1,
    bg=gettheme()['bg'],
    relief='flat'
).pack(side='left')

search_input = tkinter.Entry(top_frame,
    fg=gettheme()['light'],
    bg=gettheme()['bg'],
    relief='flat',
    font=(gettheme()['font'], 20),
    insertbackground=gettheme()['light'],
)
search_input.pack(side='left', ipady=5)
search_input.focus_set() 

def search(rec_frame, title_label):
    videos = magicwaves.search(search_input.get())
    for video in videos:
        video_frame = tkinter.Frame(win,
            bg=gettheme()['bg'],
        )
        video_frame.pack()

        title_label.config(text='Search results')

        url = video['thumbnails'][0]['url']
        r = urllib.request.urlopen(url).read()
        open(f'temp/thumbnails/{video["id"]}.jpg', 'wb').write(r)
        load = Image.open(f'temp/thumbnails/{video["id"]}.jpg').resize((180, 101), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        image_label = tkinter.Buttom(video_frame,
            image=render)
        image_label.pack(side='left', anchor='w')

        image_label['image'] = render
        image_label.config(image=render)
        image_label.image = render

        tkinter.Button(video_frame,
            text=video['channel']['name'],
            command=None,
            font=(gettheme()['font'], 11),
            fg=gettheme()['fg'],
            bg=gettheme()['bg'],
            relief='flat'
        ).pack(side='right', anchor='e')

        tkinter.Button(video_frame,
            text=video['title'],
            command=None,
            font=(gettheme()['font'], 15),
            fg=gettheme()['light'],
            bg=gettheme()['bg'],
            relief='flat'
        ).pack(side='right', anchor='e')

        rec_frame.destroy()

tkinter.Button(top_frame,
    command=search,
    text='👤',
    height=1,
    font=(gettheme()['font'], 20),
    fg=gettheme()['fg'],
    bg=gettheme()['bg'],
    relief='flat'
).pack(side='right')

tkinter.Button(top_frame,
    command=lambda: search(recommendation_frame, title),
    text='🔍',
    height=1,
    font=(gettheme()['font'], 20),
    fg=gettheme()['fg'],
    bg=gettheme()['bg'],
    relief='flat'
).pack(side='right')

rpc = magicwaves.start_rpc()
rpc.update(state='Listening to music', details='In main menu', start=time.time(), large_image='icon')

win.mainloop()
