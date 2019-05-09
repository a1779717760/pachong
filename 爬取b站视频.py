import requests
import json
import pprint

#offset=31
for i in range(10):
    url = 'http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset={i}1&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'.format(i=i)
    response = requests.get(url)
    data = response.json()
    #pprint.pprint(data)
    items = data['data']['items']
    #pprint.pprint(items)
    for m in items:
        n = m['item']
        #pprint.pprint(n)
        id = n['id']
        url = 'http://api.vc.bilibili.com/clip/v1/video/detail?video_id={id}&need_playurl=1'.format(id=id)
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

        response = requests.get(url)
        data = response.json()
        #pprint.pprint(data)
        video_playurl = data['data']['item']['video_playurl']
        response = requests.get(video_playurl,headers = headers)
        video_size = data['data']['item']['video_size']
        print(video_playurl)
        # print(description)
        with open(video_size+".mp4",mode = 'wb') as f:
            f.write(response.content)









