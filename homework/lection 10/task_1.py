# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


# Здесь пишем код
def generate_random_name():
    letters = list(string.ascii_lowercase)
    while True:
        name = ""
        for i in range(2):
            for ii in range(random.randint(1, 15)):
                name = name + random.choice(letters)
            if i == 0:
                name += " "
        yield name

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))