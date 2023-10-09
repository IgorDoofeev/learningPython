s = lambda a, b: a + b

print(s(1, 2))

lst = [5, 3, 0, -6, -8, 10, 1]

def get_filter(a, filter=None):
    if filter is None:
        return a

    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res


r = get_filter(lst, lambda x: x % 2 == 0)
print(r)