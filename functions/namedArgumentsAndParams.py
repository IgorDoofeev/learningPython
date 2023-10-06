# Вычисление объема паралелепипеда
def get_V(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a * b * c


# v = get_V(1, 2, 3)
# Вариант с именоваными аргументами
v = get_V(b=1, a=2, c=3)
print(v)


# Формальные параметры
def cmp_str(s1, s2, reg=False, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()

    return s1 == s2


print(cmp_str('Python ', ' Python'))


def add_value(value, lst=None):
    if lst is None:
        lst = []

    lst.append(value)
    return lst


l = add_value(1)
l = add_value(2, l)
print(l)
