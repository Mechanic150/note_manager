from datetime import datetime, timedelta
now_data = datetime.today().date().strftime('%d:%m:%Y') #получаем текущую дату в str
now_data_conv = datetime.strptime(now_data, '%d:%m:%Y').date() #конвертируем в datetime для использования timedelta
print('Текущая дата: ', now_data)
while True:
    issue_date = input('Укажите дату истечения заметки в формате ДД:ММ:ГГ: ')
    try:
        valid_date = datetime.strptime(issue_date, '%d:%m:%Y') #проверка формата ввода даты
        break
    except ValueError:
        print('Заданный формат даты не принимается, пропрбуйте еще раз!')
issue_date_conv = datetime.strptime(issue_date, '%d:%m:%Y').date() #конвертация введенной даты из str в datetjme
day_to_deadline = issue_date_conv - now_data_conv
if issue_date_conv == now_data_conv:
    print('Внимание! Срок заметки истекает сегодня!')
elif day_to_deadline < timedelta(days=0):
    print('Срок заметки истек!')
elif day_to_deadline < timedelta(days=1):
    print('Внимание! Срок заметки истекает через 1 день!')
elif day_to_deadline < timedelta(days=2):
    print('Внимание! Срок заметки истекает через 2 дня!')
else: print('Дней до истечения заметки: ', day_to_deadline.days)