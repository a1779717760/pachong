import requests
import json
import pprint

url = 'https://m.weibo.cn/api/container/getIndex?containerid=2304136342288605_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page='
#pprint.pprint(requests.get(url).json())

for i in range(10):
    response = requests.get(url.format(i))
    data = response.json()
    cards = data['data']['cards']
    #print(mid)
    for mid in cards:
        if mid.get('mblog',None):
            id = mid['mblog']['mid']
            response = requests.get('https://m.weibo.cn/comments/hotflow?id={id}&mid={id}&max_id_type=0'.format(id=id))

            data = json.loads(response.text)
            # pprint.pprint(data)
            users = data['data']['data']            #
            for user in users:
                # users['screen_name']
                print(user['text'])
                print(user['user']['screen_name'])


