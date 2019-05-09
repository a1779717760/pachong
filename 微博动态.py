import requests
import json
import pprint
import weiboshouye import *

response = requests.get('https://m.weibo.cn/comments/hotflow?id=4363809516726222&mid=4363809516726222&max_id_type=0')

data = json.loads(response.text)
#pprint.pprint(data)
users = data['data']['data']
#
for user in users:
    #users['screen_name']
    print(user['text'])
    print(user['user']['screen_name'])

