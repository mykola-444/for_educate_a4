from tkinter import Tk, Button

from class_varification__ import Verification


class V2(Verification):

    def __init__(self, login, password, age):  # перевизначаємо метод __init__
        #Verification.__init__(self, login, password)  # викликаємо батьківський метод
        super().__init__(login, password)  # аналогічний запис (без self) - шукає методи у батьківських класах
        self.__save()  # під час реєстрації відразу збергігаємо
        self.age = age  # додатковий параметр який розширює функціонал

    def __save(self):  # перевизначаємо метод save ( і робимо приватним - використовується тільки в середині класу
        with open('user') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError('already exist')
        super().save()  # аналогічний запис (без self)
        # Verification.save(self)  # викликаємо батьківський метод

    def show(self):
        return self.login, self.password


# x = V2('Petro3', '123456789')
y = V2('Vlad', '567789012', 26)
