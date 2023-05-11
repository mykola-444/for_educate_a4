class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()


class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')

