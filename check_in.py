
def registration(user_id, cipher):     #Регистрация
    with open('data.txt', 'r') as data:
        for i in data:
            if i.split(':')[0] == str(user_id):
                old_data = data.read()
                new_data = old_data.replace(i, str(user_id) + ":" + str(cipher) + '\n')
                readd(new_data)
        else:
            add(user_id, cipher)


def add(user_id, cipher):   #Запись нового пользователя
    with open('data.txt', 'a') as data:
        data.writelines(str(user_id) + ":" + str(cipher) + '\n')


def readd(new_data):    #Перезапись пользователя
    with open('data.txt', 'w') as data:
        data.write(new_data)


def get_user_cipher(user_id):   #Запрос на получение шифра группы пользователя
    data = open('data.txt', 'r')
    for i in data:
        if i.split(':')[0] == str(user_id):
            cipher = i.split(':')[1].strip('\n')
            data.close()
            return cipher