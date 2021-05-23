"""GUI for MagicWaves YouTube Downloader"""

"""IF PROBLEMS OCCUR, START 'guirunner.py'!"""

import magicwaves

import os
import yaml
import time
import shutil
import tkinter
import keyboard
import webbrowser
import urllib.request

from PIL import Image, ImageTk

cwd = os.getcwd()

def cleartemp():
    try:
        shutil.rmtree(cwd + '\\temp\\')
        os.mkdir
    except:
        pass

cleartemp()

def gettheme():
    theme = {}
    theme['fg'] = 'white'
    theme['bg'] = '#0E0F13'
    theme['font'] = 'Yu Gothic UI'
    theme['title'] = 'Yu Gothic UI Bold'
    theme['light'] = '#008AE6'
    theme['warn'] = '#fc9d19'
    theme['critical'] = '#fc3b19'
    theme['ok'] = '#28ff02'
    return theme

win = tkinter.Tk()
win.title('MagicWaves')
win.config(bg=gettheme()['bg'])
win.geometry('600x653')
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

globals()['searches'] = 0

def search(rec_frame, title_label):
    if globals()['searches']:
        pass
        # not first search
        # win.destroy()

    # win = tkinter.Tk()

    videos = magicwaves.search(search_input.get())
    for video in videos:
        video_frame = tkinter.Frame(win,
            bg=gettheme()['bg'],
        )
        video_frame.pack()

        title_label.config(text='Search results')

        # I made functions so the behaviour of the video buttons is easier customizable

        def image_clicked(url):
            webbrowser.open(url)

        def channel_clicked(url):
            webbrowser.open(url)
        
        def title_clicked(url):
            if keyboard.is_pressed('shift'):
                magicwaves.show(magicwaves.download(url))
            else:
                magicwaves.play(magicwaves.download(url))

        # Download result thumbnail image
        url = video['thumbnails'][0]['url']
        r = urllib.request.urlopen(url).read()
        open(f'temp/thumbnails/{video["id"]}.jpg', 'wb').write(r)
        load = Image.open(f'temp/thumbnails/{video["id"]}.jpg').resize((180, 101), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        # Display result thumbnail image
        image_label = tkinter.Button(video_frame,
            image=render,
            command=lambda url=video['link']: image_clicked(url)
        )
        image_label.pack(side='left', anchor='w')

        image_label['image'] = render
        image_label.config(image=render)
        image_label.image = render

        tkinter.Button(video_frame,
            text=video['duration'] + ' • ' + video['channel']['name'],
            command=lambda url=video['channel']['link']: channel_clicked(url),
            font=(gettheme()['font'], 11),
            fg=gettheme()['fg'],
            bg=gettheme()['bg'],
            relief='flat'
        ).pack()#side='left', anchor='w')

        # Display the video title properly
        title = video['title'][:35]
        if len(video['title']) > 35:
            title = title + '...'

        tkinter.Button(video_frame,
            text=title,
            command=lambda url=video['link']: title_clicked(url),
            font=(gettheme()['font'], 15),
            fg=gettheme()['light'],
            bg=gettheme()['bg'],
            relief='flat',
            width=35,
        ).pack(side='right')#, anchor='e')

        rec_frame.destroy()

        globals()['searches'] += 1

# top right icons
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

def search_pressed(unused):
    search(recommendation_frame, title)

keyboard.on_press_key('enter', search_pressed)

win.mainloop()
