import pandas as pd     #Импорт библиотеки Pandas

file_exel = 'raspisanie.xlsx'

schedule = pd.read_excel(file_exel)   #С помощью метода read_excel() считываем таблицу

mainSchedule = {}   #Основное расписание

ciphersOfGroups = list(schedule[0:0])
ciphersOfGroups.__delitem__(0)
ciphersOfGroups.__delitem__(0)

for i in range(ciphersOfGroups.__len__()):    #Формируем словарь по принципу КЛЮЧ - шифр группы, ЗНАЧЕНИЕ - список пар
    mainSchedule.__setitem__(ciphersOfGroups[i], schedule[ciphersOfGroups[i]])

for j in mainSchedule:      #Заменяем пропуски в расписаниями на "Пары нет"
    for l in range(len(mainSchedule[j])):
        if mainSchedule[j][l] == ' ':
            mainSchedule[j][l] = 'Пары нет'

board_ciphers = {'1': [], '2': [], '3': [], '4': [], '5': []}

for n in range(ciphersOfGroups.__len__()):
    word = str(ciphersOfGroups[n])
    for g in ciphersOfGroups[n]:
        if g != '0' and g != '1' and g != '2' and g != '3' and g != '4' and g != '5' and g != '6' and g != '7' and g != '8' and g != '9' and g != 'а':
            word = word[:-1]
    board_ciphers[word[-1]].append(ciphersOfGroups[n])

print('Schedule created successfully.')
