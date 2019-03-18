# тест
import vk_api 
from vk_api.longpoll import VkLongPoll, VkEventType


def main():
    login = input('Login: ')
    password = input('Password: ')
    session = vk_api.VkApi(login, password)
    session.auth()
    vk = session.auth()
    lp = VkLongPoll(session)
    for event in lp.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение: ', event.text)

    # if vk.users.get(user_id='154597302', fields='online'):
    #     vk.messages.send(user_id='154597302', message='хуй', random_id='235')


if __name__ == '__main__':
    main()
