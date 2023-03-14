class Dog:
    species = 'Canis familiaris'
    def __init__(self, name, age):
        self.name = name
        self.age  = age
# metod exempler
    def description(self):
        return f'{self.name} is {self.age} years old'
    def speak(self, sound):
        return f'{self.name} says {sound}'

miles = Dog('Miles', 4)
miles.description()
miles.speak('Woof Woof')

print(miles.description())
print(miles.speak('Woof Woof'))
print(miles.speak('Boow Boow'))