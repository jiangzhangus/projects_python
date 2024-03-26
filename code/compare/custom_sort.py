

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age;

persons = []
persons.append(Person("John", 40))
persons.append(Person("Zhang", 30))

print("----compare by name ------")
s = sorted(persons, key=Person.get_name)
for p in s:
    print(p.get_name(), p.get_age())


print("----compare by age ------")
s = sorted(persons, key=Person.get_age)
for p in s:
    print(p.get_name(), p.get_age())

