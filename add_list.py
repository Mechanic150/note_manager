username = input('Ваше имя: ')
title = input('Название заметки: ')
title1 = input('Заголовок 1: ')
title2 = input('Заголовок 2: ')
content = input('Описание заметки: ')
status = input('Статус заметки: ')
created_date = input('Дата создания заметки в формате ДД.ММ.ГГГГ: ')
issue_date = input('Дата истечения заметки в формате ДД.ММ.ГГГГ: ')
titles = [title, title1, title2]
print('Имя пользователя: ', username)
print('Заголовок заметки: ', titles)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', created_date)
print('Дата истечения заметки: ', issue_date)