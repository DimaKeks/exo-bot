from spiski import *
from ugra import *


def write_msg(user_id,text):
    vk_bot.method('messages.send', {'user_id':user_id,'message': text,'random_id':random.randint(0,1000)})
def somefunc(a1):
    funcmap[a1]()

vk_bot = vk_api.VkApi(token=TOKEN)
long_pool = vk_bot.method('messages.getLongPollServer', {'need_pts':1,'lp_version':3})
server, key, ts = long_pool['server'], long_pool['key'], long_pool['ts']
print("готов к работе")
# + str(long_pool))

while True:
    a=random.randint(0,5)
    long_pool = requests.get(
        'https://{server}?act={act}&key={key}&ts={ts}&wait=500'.format(server=server,
                                                                       act='a_check',
                                                                       key=key,
                                                                       ts=ts)).json()
    update = long_pool['updates']
    print(update)
    if update [0][0] == 4:
        user_id=update[0][3]
        if 'привет' in update[0][6]:
             write_msg(user_id,privetik[a])
        elif 'давай сыграем' in update[0][6]:
            write_msg(user_id,"Можно и сыграть, но только я еще недоделан")
            write_msg(user_id,"Играем в камень ножницы бумагу")
            somefunc(1)
        else:
            write_msg(user_id,"все нормальные люди сначала здороваются")
    ts = long_pool['ts']