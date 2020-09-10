class Person:

    def __init__(self, name, surname, age=19): # конструктор класса
        self.name = name                       # атрибуты класса
        self.surname = surname
        self.age = age

    def show_info(self):
        print('Этого человека зовут {name} {surname}. Ему {age} лет. '.format(name=self.name, surname=self.surname,
                                                                              age=self.age))

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print('Ошибка! Недопустимый возраст!')


# класс Student наследуется от класса Person (наследование)
class Student(Person):
    # переопределение конструктора (полиморфизм)
    def __init__(self, name, surname, age, curse):
        Person.__init__(self, name, surname, age)
        self.curse = curse

    # переопределение метода (полиморфизм)
    def show_info(self):
        Person.show_info(self)
        print('Студент учиться на {} курсе'.format(self.curse))


person_1 = Person("Andrew", "Afanasiev") # экземпляр класса
person_1.show_info()

student_1 = Student("Ivan", "Ivanov", 19, 2)
student_1.show_info()
