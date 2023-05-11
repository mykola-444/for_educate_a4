class Person:
    name = "Igor"
    age = 4
    def __init__(self, name, age):
       self.name = name
       self.age = age
	   
    def set(self, name, age):
       self.name = name
       self.age = age

class Student (Person):
    course = 1
    def set(self, name, age, course):
       self.name = name
       self.age = age
       self.course = course
	
igor = Student("Peta", 120)
igor.set("Misha",56,3)
print(igor.age, igor.course, igor.name)

vlad = Person("DAVID", 76)
vlad.set("VLAD", 56)
print(vlad.age, vlad.name)

