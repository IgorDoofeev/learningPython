class Person:
    "This is class that describes a person"
    age = 10

    def greet(self):
        print('Hello')


print(Person.age)
print(Person.greet)
print(Person.__doc__)

# Create new class Person
harry = Person()
harry.greet()

