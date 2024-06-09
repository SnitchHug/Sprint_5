from random import randint


class Person:
    user_name = 'Виктор'
    email = f'viktortsarkov9777@ya.ru'
    password = f'12345Qwe'


class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@ya.ru'
    password = f'{randint(1000, 9999)}Qwe'
