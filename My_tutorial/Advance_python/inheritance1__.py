from tkinter import Tk, Button

from class_varification__ import Verification


class V2(Verification):

    def __init__(self, login, password, age):  # перевизначаємо метод __init__
        Verification.__init__(self, login, password)  # викликаємо батьківський метод
        self.__save()  # під час реєстрації відразу збергігаємо
        self.age = age  # додатковий параметр який розширює функціонал

    def __save(self):  # перевизначаємо метод save ( і робимо приватним - використовується тільки в середині класу
        with open('user') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError('already exist')
        Verification.save(self)  # викликаємо батьківський метод

    def show(self):
        return self.login, self.password


# x = V2('Petro3', '123456789')
# y = V2('Vlad', '56789012', 26)


#наслідування від класу tkinter
class My_app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('400x400')
        self.setUI()

    def setUI(self):
        Button(self, text="OK").pack()


root = My_app()
root.mainloop()
