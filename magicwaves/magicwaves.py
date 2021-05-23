import os
import shutil
import requests
import threading
import webbrowser
import youtube_dl
import pypresence

import youtubesearchpython as ysp

cwd = os.getcwd()

def start_rpc():
    rpc = pypresence.Presence(840292943738699777)
    rpc.connect()

    return rpc

def download(url):
    name = url.split('=')[1]
    path = f'{cwd}\\temp\\audio\\{name}.wav'

    ydl_opts = {
        'outtmpl': path,
        }

    with youtube_dl.YoutubeDL(ydl_opts) as downloader:
        downloader.download([url])
    
    return path
    
def play(path):
    """Plays a song"""
    os.system(f'start {path}')

def show(path):
    """Shows a directory/file in the file explorer"""
    if '.' in path.replace('\\', '/').split('/')[-1]:
        # Is a file
        path = path.replace('\\', '/').split('/')[:-1] # use the directory, not file
    os.system(f'explorer.exe {path}')

def search(query):
    results = ysp.VideosSearch(query, limit=5).result()['result']

    return results

        # image_url = video['thumbnails'][0]
        # filename = video['id']

        # r = requests.get(image_url, stream=True)

        # if r.status_code == 200:
        #     r.raw.decode_content = True
            
        #     with open(f'{cwd}\\temp\\thumbnails\\{filename}.jpg', 'wb') as f:
        #         shutil.copyfileobj(r.raw, f)
                
        #     print('Downloaded thumbnail ID' + filename)
        # else:
        #     print('[ERROR] Image Couldn\'t be retreived (HTTPS error)')

def web_open(video_id):
    webbrowser.open('https://youtu.be/' + video_id)
