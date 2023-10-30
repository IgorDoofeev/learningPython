class Point:  # create class
    "Класс для предоставление координат"  # Документация для вызова через __doc__
    color = 'red'  # first attribute
    circle = 2  # second attribute


Point.color = 'Black'  # Changing an attribute
print(Point.color)
print(Point.circle)  # Calling an attribute
print(Point.__dict__)  # View all attribute

a = Point()  # Creating an Instance of a Class

Point.type_pt = 'disc'

setattr(Point, 'top', 1)  # function for create attribute
getattr(Point, 'no', False)  # Get attribute
del Point.top  # Delete attribute
hasattr(Point, 'color')  # Info attr
delattr(Point, 'color')  # Delete attribute
hasattr(Point, 'color')  # Info attr

print(Point.__doc__)
