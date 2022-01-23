from random import randint

random_number = randint(1, 10)
user_input = None
count = 0

while user_input != random_number:
    random_number = randint(1, 10)
    user_input = int(input('Введите число: '))
    if user_input != random_number:
        count += 1
        print('Попробуй еще раз')
    else:
        count += 1
        print('Ты победил', count)
print('Количество попыток:', count)


