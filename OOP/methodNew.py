class Point:
    def __new__(cls, *args, **kwargs):  # cls ссылается на текущий экземпляр класса на класс Поинт
        print('вызов __new__ для ' + str(cls))
        return super().__new__(cls)  # Вернем адрес нового созданого объекта,


    def __init__(self, x=0, y=0):  # self будет ссылаться на создаваемый экземпляр класса
        print('вызов __init__ для ' + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt)