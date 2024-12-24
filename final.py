username = input('Ваше имя: ')
title = input('Название заметки: ')
title1 = input('Заголовок 1: ')
title2 = input('Заголовок 2: ')
content = input('Описание заметки: ')
status = input('Статус заметки: ')
created_date = input('Дата создания заметки в формате ДД.ММ.ГГГГ: ')
issue_date = input('Дата истечения заметки в формате ДД.ММ.ГГГГ: ')
titles = [title, title1, title2]
note = [
    username,
    titles,
    content,
    status,
    created_date[:5],
    issue_date[:5]
]
print(note)