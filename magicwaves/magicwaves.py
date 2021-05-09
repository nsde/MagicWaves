import os
import shutil
import requests
import webbrowser
import youtube_dl
import pypresence

import youtubesearchpython as ysp

cwd = os.getcwd()

def start_rpc():
    rpc = pypresence.Presence(840292943738699777)
    rpc.connect()
    return rpc

def play_video(video_id, video_name):
    videoUrl = 'https://youtu.be/' + video_id
    ydl_opts = {
        'outtmpl': f'{cwd}\\temp\\audio\\{video_id}.wav',
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([videoUrl])

def search(query):
    print(f'Searching \'{query}\'...')
    results = ysp.VideosSearch(query, limit=12).result()['result']

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
