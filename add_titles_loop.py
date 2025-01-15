titles = []
while True:
    title = input('Введите название заметки: ')
    if title == '':
        print('Название нужно ввести обязательно!')
    else: break
while True:
    answ = input('Нажмите Enter, чтобы добавить еще заголовок или введите Стоп для завершения: ')
    if answ == '':
        title_1 = input('Введите название заголовка: ')
        if title_1 == '':
            print('Заголовок нужно ввести обязательно!')
        if title_1 != '':
            titles.append(title_1)
    if answ == 'Стоп':
        break
print('Название заметки: ', title, '\n', 'Заголовки заметки: ', titles)