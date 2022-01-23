inp_login = input('Введите логин: ')
inp_password = int(input('Введите пароль: '))
attempt = 3
task = {}
list = []
while True:
    if inp_login == 'Admin' and inp_password == 0000:
        print(f'Добро пожаловать, {inp_login}!')
        inp_ask = input('Обновить список дел? yes/no: ')
        if inp_ask == 'yes':
            inp_data = input('Введите дату: ')
            inp_task = input('Введите дело: ')
            task['data'] = inp_data
            task['task'] = inp_task
            list.append(task)
            print(task)
            print(list)
            break
        elif inp_ask == 'no' or inp_ask == '':
            print('Туду лист закрыт')
            break
    else:
        attempt -= 1
        if attempt == 0:
            print('Ваши попытки кончились')
            break
        if attempt == 1:
            print(f'Осталось {attempt} попытка')
        else:
            print(f'Осталось {attempt} попытки')
        input('Введите логин: ')
        int(input('Введите пароль: '))



# task = {}
# list = []
# inp_ask = input('Обновить список дел? yes/no: ')
# while inp_ask:
#
#     if inp_ask == 'yes':
#         inp_data = input('Введите дату: ')
#         inp_task = input('Введите дело: ')
#         task['data'] = inp_data
#         task['task'] = inp_task
#         list.append(task)
#
#         print(task)
#         print(list)
#         input('Обновить список дел? yes/no: ')
#
#     elif inp_ask == 'no' or inp_ask == '':
#         print('Туду лист закрыт')
#         break