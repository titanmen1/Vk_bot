import requests
import vk_api
from vk_api.upload import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
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

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Цитата', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()
keyboard.add_button('help', color=VkKeyboardColor.DEFAULT)




def messages_user():
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

            # Слушаем longpoll, если пришло сообщение то:
            if event.text == 'Цитата':  # Если написали заданную фразу
                if event.from_user:  # Если написали в ЛС

                    # Отправка фотографии
                    file = 'image/' + str(random.randint(1, 30)) + '.jpg'
                    photo1 = upload.photo_messages(file)

                    vk.messages.send(  # Отправляем сообщение
                        user_id=event.user_id,
                        message=pars()[random.randint(1, 146)],
                        random_id=get_random_id(),
                        attachment='photo{}_{}'.format(photo1[0]['owner_id'], photo1[0]['id']),
                        keyboard=keyboard.get_keyboard(),
                    )
                    # vk.messages.send(  # Отправляем сообщение
                    #     user_id=event.user_id,
                    #     message='1',
                    #     random_id=get_random_id(),
                    #     keyboard=keyboard.get_keyboard(),
                    # )


                    return messages_user()
            if event.text == 'help':
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        message="Слушай браток, я буду тебя развлекать, пока ты чалишься на нарах. Вводи команду 'Цитата' и я пришлю четкую цитату про нашу не легкую жизнь",
                        random_id=get_random_id(),
                        keyboard=keyboard.get_keyboard(),
                    )




if __name__ == '__main__':


    messages_user()

    # msg()







