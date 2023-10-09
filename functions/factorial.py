""" Вычисление факториала с помощью рекурсивной функции
n! = 1 * 2 * 3 * ... * n
n! = (n-1)! * n
"""

def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n - 1)


p = fact(7)
print(p)
