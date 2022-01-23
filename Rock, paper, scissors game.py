import random
list_1 = ['Камень', 'Ножницы', 'Бумага']
user_inp = input('Камень? Ножницы? Бумага?:')
random_element = random.choice(list_1)

while user_inp == random_element:
    print('Повтор?')
    user_inp = input('Камень? Ножницы? Бумага?: ')
    random_element = random.choice(list_1)

if user_inp == 'Бумага' and random_element == 'Камень':
    print('Ты победил')
elif user_inp == 'Ножницы' and random_element == 'Бумага':
    print('Ты победил')
elif user_inp == 'Камень' and random_element == 'Ножницы':
    print('Ты победил')
else:
    print('Компьтер победил')

print('Игрок', user_inp)
print('Компьтер', random_element)






