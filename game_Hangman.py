'''
Угадайка слов

Описание проекта: программа загадывает слово, а пользователь должен его угадать на основании вопроса. Изначально все
буквы слова неизвестны. Также рисуется виселица с петлей. Пользователь предлагает букву, которая может входить в это
слово. Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове. Если
такой буквы нет, к виселице добавляется круг в петле, изображающий голову. Пользователь продолжает отгадывать буквы
до тех пор, пока не отгадает всё слово. За каждую неудачную попытку добавляется еще одна часть туловища висельника
(обычно их 6: голова, туловище, 2 руки и 2 ноги).
'''

import random
import words_for_game_Hangman as wh


# функция получение случайного слова из списка
def get_word():
    word, question = random.choice(list(wh.words_questions.items()))
    return word.upper(), question


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


# проверка корректности вводимых данных пользователя
def is_correct_input(w):
    flag = False
    if not w.isalpha():
        print('Допустимы только слова и буквы. Попробуйте еще раз')
    else:
        flag = True
    return flag


# Проверка на повторы
def check_repeat(w, guessed_letters, guessed_words):
    flag = False
    if len(w) == 1 and w in guessed_letters:
        print(f'Вы уже называли букву "{w}". Попробуйте еще раз.')
    elif len(w) > 1 and w in guessed_words:
        print(f'Вы уже называли слово "{w}". Попробуйте еще раз.')
    else:
        flag = True
    return flag


# Функция проверяет есть ли такая буква
def is_letter_in_hidden_word(w, word, word_completion):
    new_word_completion = ''
    for i in range(len(word)):
        if word[i] == w:
            new_word_completion += w
        else:
            new_word_completion += word_completion[i]
    return new_word_completion


# функция основного процесса игры
def play(word, question):
    print('\nДавайте играть в угадайку слов!')
    word_completion = '_' * len(word)   # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                     # сигнальная метка о выигрыше
    guessed_letters = []                # список уже названных букв
    guessed_words = []                  # список уже названных слов
    tries = 6                           # количество попыток
    print(display_hangman(tries))
    print(f'Я загадал слово и оно состоит из {len(word)} букв')
    print(f'Так называется - "{question}". Что это?\n')
    print(f'У вас есть {tries} попыток, чтобы отгадать. Поехали!')
    print(word_completion)
    while tries > 0:
        w = input(f'\nПопытка № {abs(tries - 7)}. Введите букву или слово целиком: ').upper()
        if is_correct_input(w) and check_repeat(w, guessed_letters, guessed_words):
            if w == word:  # если угадали слово целиком
                guessed = True
                break
            elif len(w) == 1:  # если названа буква
                tries -= 1
                guessed_letters.append(w)
                word_completion = is_letter_in_hidden_word(w, word, word_completion)
                print(display_hangman(tries))
                if w in word_completion:
                    print(f'Буква "{w}" есть в этом слове!\nПовторю вопрос - "{question}"\n{word_completion}')
                else:
                    print(f'Такой буквы нет\nПовторю вопрос - "{question}"\n{word_completion}')
                print(f'Осталось попыток: {tries}')
            elif len(w) > 1:  # если названо неверное слово
                tries -= 1
                guessed_words.append(w)
                print(display_hangman(tries))
                print(f'"{w}" - неверное слово\nПовторю вопрос - "{question}"\n{word_completion}')
                print(f'Осталось попыток: {tries}')
    if guessed:
        print(f'Поздравляю, вы угадали слово "{word}"! Вы победили!')
    else:
        print(f'Вы не смогли угадать слово "{word}". В следующий раз обязательно повезет!')


# запуск игры
play(*get_word())

# запрос повторной игры
repeat_play = input('\nСыграем еще раз?\nд - Повторить игру\nн - Выйти из игры\n')
if repeat_play.upper() == 'Д':
    play(*get_word())
