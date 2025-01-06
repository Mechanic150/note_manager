while True:
    title = input('Введите название заметки: ')
    if title == '':
        print('Заголовок нужно ввести обязательно!')
    else: break
title_1 = input('Введите заголовок 1 или нажмите Enter, чтобы продолжить: ')
title_2 = input('Введите заголовок 2 или нажмите Enter, чтобы продолжить: ')
if title_1 == '' and title_2 == '':
    print('Название заметки: ', title)
    print('Заголовков нет')
if title_2 == '' and title_1 != '':
    print('Название заметки: ', title)
    print('Заголовки заметки: ')
    print('- ', title_1)
if title_1 != '' and title_2 != '':
    print('Название заметки: ', title)
    print('Заголовки заметки: ')
    print('- ', title_1)
    print('- ', title_2)
if title_1 == '' and title_2 != '':
    print('Название заметки: ', title)
    print('Заголовки заметки: ')
    print('- ', title_2)