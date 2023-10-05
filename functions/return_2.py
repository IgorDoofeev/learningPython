# Нет явного указания что должна возвращать функция, соответственно результата
# не будет
def get_sqrt(x):
    res = None if x < 0 else x ** 0.5


result = get_sqrt(49)
print(result)


def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res


result = get_sqrt(49)
print(result)


def get_max(a, b):
    return a if a > b else b


x, y, z = 5, 7, 10
print(get_max(x, get_max(y, z)))


# Определение четного числа с помощью функции и цикла
def even(x):
    return x % 2 == 0


for i in range(1, 20):
    if even(i):
        print(i)
