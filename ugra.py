import random
import requests
import vk_api
from config import *

def write_msg(user_id,text):
    vk_bot.method('messages.send', {'user_id':user_id,'message': text,'random_id':random.randint(0,1000)})

vk_bot = vk_api.VkApi(token=TOKEN)
long_pool = vk_bot.method('messages.getLongPollServer', {'need_pts':1,'lp_version':3})
server, key, ts = long_pool['server'], long_pool['key'], long_pool['ts']

def func1():
    while True:
        long_pool = requests.get(
            'https://{server}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                           act='a_check',
                                                                           key=key,ts=ts)).json()
        update = long_pool['updates']
        print(update)
        if update [0][0] == 4:
            user_id=update[0][3]
            ugra1 = random.randint(1,3)
            if "камень" in update[0][6]:
                ugra2 = 1
                if (ugra2-ugra1)==0:
                    write_msg(user_id,'ничья')
                    write_msg(user_id,"давай еще")
                elif (ugra2-ugra1)==0:
                    write_msg()
                else:
                    write_msg()
            elif "ножницы" in update[0][6]:
                write_msg()
            elif "бумага" in update[0][6]:
                write_msg()
            else:
                write_msg(user_id,"не мухлюй, только камень, ножницы или бумага")
        ts = long_pool['ts']
funcmap={1:func1()}