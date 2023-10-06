# *args - позволяет принять произвольное число фактических аргуметов (упаковывает в кортеж)
# **kwargs - позволяет принять произвольное число именованных аргуметов(упаковывает в словарь)

def os_path(*args, **kwargs):
    path = '\\'.join(args)
    return path


p = os_path('1', '2', '4', '\\asd', sep='/', trim=True)

print(p)

# Пример распаковки
x, y = (1, 2)
print(f'x = {x}')
print(f'y = {y}')

x, *y = (1, 2, 3, 4)
print(f'x = {x}')
print(f'y = {y}')

*x, y, z = 'Hello Python!'
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')

# Пример упаковки
a = [1, 2, 3]

d = -5, 5
print(range(*d))
print(*range(*d))

print({*d})