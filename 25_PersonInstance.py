class Person:
    name = "Person"

    def __init__(self, name=None):
        self.name = name


baki = Person("Bake")
print(Person.name, baki.name)

issa = Person()
issa.name = "Issa"
print(Person.name, issa.name)
