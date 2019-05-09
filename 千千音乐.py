import requests
import re
import pprint
# mp3_url = "http://play.taihe.com/data/music/songlink"
#
# response = requests.get(mp3_url)
#
# with open("后来.mp3",mode = 'wb') as f:
#     f.write(response.content)
def get_url(s):
    data = {
        'songIds': s,
        'hq': '0',
        'type': 'm4a,mp3',
        'rate':'',
        'pt': '0',
        'flag': '-1',
        's2p': '-1',
        'prerate': '-1',
        'bwt': '-1',
        'dur': '-1',
        'bat': '-1',
        'bp': '-1',
        'pos': '-1',
        'auto': '-1',
    }
    response = requests.post(url='http://play.taihe.com/data/music/songlink',data=data)
    music_lite = response.json()['data']['songList']
    for music in music_lite:
        artist_name = music['artistName']
        song_name = music['songName']
        song_link = music['songLink']
        yield artist_name,song_name,song_link

def get_song():
    response = requests.get('http://music.taihe.com/artist/7994')
    response.encoding = response.apparent_encoding
    songid = re.findall('href="/song/(\d+)',response.text,re.S)
    return songid

songids = get_song()
s = ",".join(songids)
g = get_url(s)
for i in g:
    response = requests.get(i[2])
    with open(i[1]+".mp3",mode = 'wb') as f:
        f.write(response.content)