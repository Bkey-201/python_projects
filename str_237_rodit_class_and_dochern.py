class Dog:
    species = 'Canis familiaris'
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        # self.breed = breed
# metod exempler
    def description(self):
        return f'{self.name} is {self.age} years old'
    def speak(self, sound):
        return f'{self.name} says {sound}'
class JackRussellTerrier(Dog):
    pass
class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4, 0)
buddy = Dachshund("Buddy", 9,0)
jack = Bulldog("Jack", 3,0)
jim = Bulldog("Jim", 5,0)

print(type(miles))
print(isinstance(miles, Dog))
print(isinstance(miles, Bulldog))
print(isinstance(miles, Dachshund))


# num_letters = len("four")
# print(num_letters)