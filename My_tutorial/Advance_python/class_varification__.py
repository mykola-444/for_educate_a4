class A:
    def a(self):
        print('A')


class B:
    def a(self):
        print('B')


class C(B):
    def a(self):
        print('C')


class D(C, A):
    def a(self):
        super().a()  # gjcbyf' шукати в глибину  спочатку в С потім в А
        super(B, self).a()
        print(self.__class__.__mro__)  # виводить порядок пошуку


D().a()


class Verification:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):  # робимо приватним - використовується тільки в середині класу
        if len(self.password) < 8:
            raise ValueError('veak pass')

    def save(self):
        with open('user', 'a') as r:
            r.write(f'{self.login, self.password}' + '\n')
