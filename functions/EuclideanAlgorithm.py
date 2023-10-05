import time

''' - Первый вариант (просто но медленно)
"""Принцип работы алгоритма евклида с помощью функций. Проведение тестов
    и коментарии к функции
    Пока a != b
        Находим большее среди a и b
        уменьшаем большее на величину меньшего

        выводим полученое значение величины a или b
"""

def get_nod(a, b):
    """Вычисляется НОД для натуральных чисел a и b
        по алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


def test_nod(func):
    # --- тест 1 --------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('test1 - ok')
    else:
        print('test1 - fail')

    # --- тест 2 --------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('test2 - ok')
    else:
        print('test2 - fail')

    # --- тест 3 ---------------
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('test 3 - ok')
    else:
        print('test3 - fail')

test_nod(get_nod)
res = get_nod(18, 24)
print(res)
help(get_nod)
'''

""" Второй варинт (правильный)
    
    Через остаток от деления.
    Пока меньшее число больше 0
        большему числу присваемвам остаток
        от деления на меньшее число
    выводим большее число
"""
def get_nod(a, b):
    """Вычисляется НОД для натуральных чисел a и b
        по быстрому алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def test_nod(func):
    # --- тест 1 --------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('test1 - ok')
    else:
        print('test1 - fail')

    # --- тест 2 --------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('test2 - ok')
    else:
        print('test2 - fail')

    # --- тест 3 ---------------
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('test 3 - ok')
    else:
        print('test3 - fail')

test_nod(get_nod)
res = get_nod(18, 24)
print(res)
help(get_nod)
