'''
Угадайка чисел
Описание проекта: программа генерирует случайное целое число в заданном диапазоне и просит пользователя угадать
это число. Если догадка пользователя больше случайного числа, то программа должна вывести сообщение
'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести
сообщение 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, то программа должна
поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
'''


import random
from correct_ending_of_numerals import correct_ending_of_numerals as cor_num

def is_int_num(user_num):
    # Функция проверяет число ли ввел пользователь
    if user_num.isdigit() and left_limit <= int(user_num) <= right_limit:
        return True
    else:
        return False


def min_num_try(left_limit, right_limit):
    # Функция подсчитывает Какое наименьшее число догадок нужно сделать пользователю, чтобы гарантированно угадать
    # загаданное число в пределе от left_limit до right_limit
    from math import log, ceil

    num = right_limit - left_limit
    numb_attempts = ceil(log(num + 1, 2))
    return numb_attempts

print('Добро пожаловать в числовую угадайку!')
print()
print('Я загадаю ЦЕЛОЕ число, а вы попробуете отгадать. В каких пределах мне загадать число?')
left_limit = int(input('Укажите нижнюю границу: '))
right_limit = int(input('Укажите верхнюю границу: '))

while right_limit <= left_limit:
    right_limit = int(input('Верхняя граница должны быть больше нижней. Укажите верхнюю границу заново: '))

random_num = random.randint(left_limit, right_limit)
print()
print(f'Я загадал целое число в промежутке от {left_limit} до {right_limit} (включительно)!')

count_try = 0
reference_try = min_num_try(left_limit, right_limit)
while True:
    print()
    user_num = input('Как вы думаете, какое это число? ')
    if not is_int_num(user_num):
        print(f'А может быть все-таки введем целое число от {left_limit} до {right_limit}?')
        continue
    user_num = int(user_num)
    count_try += 1
    if user_num == random_num:
        print()
        print('**********************//////!!!!!!**********************')
        print(f'Вы угадали, поздравляю!!! Я загадывал именно число {random_num}.')
        if count_try <= reference_try:
            print(f'Вам для этого потребовалось {count_try} {cor_num(count_try, 'попытка')} и это идеальный результат,')
            print(f'т.к. минимальный гарантированный результат для победы - {reference_try} {cor_num(count_try, 'попытка')}')
        else:
            print(f'Вам для этого потребовалось {count_try} {cor_num(count_try, 'попытка')}.')
            print('А вы знали, что минимальный гарантированный результат для угадывания числа')
            print(f'в диапазоне от {left_limit} до {right_limit} это {reference_try} {cor_num(count_try, 'попытка')}?')
        break
    elif user_num < random_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        continue
    elif user_num > random_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue

print('________________________________________________________')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
