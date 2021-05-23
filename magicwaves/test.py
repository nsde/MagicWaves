import youtubesearchpython as ysp

results = ysp.VideosSearch('hello', limit=5).result()['result']
print(results[0]['duration'])