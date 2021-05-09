import youtubesearchpython as ysp

videosSearch = ysp.VideosSearch('bonez roadrunner', limit=12)

print(videosSearch.result()['result'][0]['channel']['name'])
