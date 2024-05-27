### Classes ###

class MyEmptyPerson:
    pass #It skips the error in the code

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):
        pass

my_person = Person('Mike', 'Treyu')
print(my_person)

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person('Mike', 'Treyu')
print(f'{my_person.name} {my_person.surname}')

class Person:
    def __init__(self, name, surname):
        self.full_name = f'{my_person.name} {my_person.surname}'

my_person = Person('Mike', 'Treyu')
print(my_person.full_name)

class Person:
    def __init__(self, name, surname, alias = 'without alias'):
        self.full_name = f'{name} {surname} ({alias})'

    def walk(self):
        print(f'{self.full_name} is walking')

my_person = Person('Mike', 'Treyu')
print(my_person.full_name)
my_person.walk()

my_other_person = Person('Mike', 'Treyu', 'Miketreyu')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Shiva (the destroyer of worlds)'
print(my_other_person.full_name)



class Person:
    def __init__(self, name, surname, alias = 'without alias'):
        self.full_name = f'{name} {surname} ({alias})' #Public
        self.__name = name #Private

    def get_name (self):
        return self.__name 

    def walk(self):
        print(f'{self.full_name} is walking')

my_person = Person('Mike', 'Treyu')
print(my_person.full_name)
#print(my_person.__name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person('Mike', 'Treyu', 'Miketreyu')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Shiva (the destroyer of worlds)'
print(my_other_person.full_name)

