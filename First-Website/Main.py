
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year


if __name__ == "__main__":
    person = Person("John", 22)
    print(person.name)
    print(person.age)
    student = Student("Dinh", 22, 2019)
    print(student.name)