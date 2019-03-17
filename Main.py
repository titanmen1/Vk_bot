import requests
import vk_api
from vk_api.upload import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import json
from vk_bot import pars

import datetime, time
# import schedule
token = 'bbfd8e6e47808fbaedf251fd3d726ffa5cc127499b3612561ea8e4f8c57fd2120e17f0fb6877ec563b750'



vk_session = vk_api.VkApi(token=token)


longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()


upload = vk_api.VkUpload(vk_session)

# file = 'image/' + str(random.randint(1,19)) + '.jpg'
#
# photo1 = upload.photo_messages(file)
#
# vk_photo_url = photo1[0]['sizes'][-1]['url']
#
#
# print(photo1, '\nLink: ', vk_photo_url)





def messages_user():
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

            # Слушаем longpoll, если пришло сообщение то:
            if event.text == 'Цитата':  # Если написали заданную фразу
                if event.from_user:  # Если написали в ЛС

                    # Отправка фотографии
                    file = 'image/' + str(random.randint(1, 19)) + '.jpg'
                    photo1 = upload.photo_messages(file)

                    print(event.text)
                    print(event.user_id)
                    vk.messages.send(  # Отправляем сообщение
                        user_id=event.user_id,
                        message=pars()[random.randint(1, 117)],
                        random_id=random.randint(1, 10000000),
                        attachment='photo{}_{}'.format(photo1[0]['owner_id'], photo1[0]['id'])
                    )
                    return messages_user()
            if event.text == 'help':
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Слушай браток, я буду тебя развлекать, пока ты чалишься на нарах. Вводи команду 'Цитата' и я пришлю четкую цитату про нашу не легкую жизнь",
                        random_id=random.randint(1, 10000000),
                    )



# def msg():
#     vk.messages.send(  # Отправляем сообщение
#         user_id=32483967,
#         message=pars()[1],
#         random_id=random.randint(1, 1000)
#     )
# schedule.every().day.at("21:30").do(msg)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

   #             pfile = post(api.photos.getMessagesUploadServer(peer_id = update['object']['user_id'])['upload_url'], files = {'photo': open('python.jpeg', 'rb')}).json()
  #              photo = api.photos.saveMessagesPhoto(server = pfile['server'], photo = pfile['photo'], hash = pfile['hash'])[0]



if __name__ == '__main__':


    messages_user()

    # msg()







