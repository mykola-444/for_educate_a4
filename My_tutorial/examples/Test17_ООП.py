class Person:
    name = "Ivan"
    age = 10

    def set(self, name,age):
        self.name = name
        self.age = age

vlad = Person()
vlad.set("Vlad", 65 )

print(vlad.name, vlad.age)

ivan  = Person()
ivan.age = 45
print(ivan.age)
