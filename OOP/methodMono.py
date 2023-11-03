class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs  # Моносостояние. При изменение локального свойства, оно меняется везде


th = ThreadData()
th1 = ThreadData()
th1.id = 3
th.attr_new = 'new_attr'
print('', th.__dict__, '\n', th1.__dict__)
