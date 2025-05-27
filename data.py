from random import randint

class Person:
    user_name = 'Ольга'
    email = f'olga_klenova_22_777@yandex.ru'
    password = f'Abc654321'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Abc'