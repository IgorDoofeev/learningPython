from accessify import private, protected


class Point:
    """
    Механизм инкапсуляции
      attribbute(без подчркиваний вначале) - публичное свойство(public)
     _attribbute - режим доступа PROTECTED(служит для обращение внутри класса и во всех его дочерних классах)
     служит только сигналом для защиты свойств. Но явно не ограничивает использование
    __attribbute - режим доступа PRIVATE (служит для обращения ТОЛЬКО внутри класса)
    """

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    #@private
    @classmethod
    def __check_value(cls, x):  # Приватный класс для проверки типа
        return type(x) in (int, float)

    def set_coord(self, x, y):  # Сеттер
        # if type(x) in (int, float) and type(y) in (int, float):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):  # Гетер
        return self.__x, self.__y


pt = Point(1, 2)
# print(pt.__doc__)
# print(pt.__x, pt._y)  # Обращение к свойствам x, y
pt.set_coord(10, 20)
pt.__check_value(6)
