class Dog1:
    pass
class Dog:
    #Атрибут класса
    species = 'Атрибут класса'
    def __init__(self, name, age):
        self.name= name
        self.age = age


buddy = Dog('Buddy', 9)
miles = Dog('Miles', 4)
charli = Dog('Charli', 5)

print(buddy.name)
print(buddy.age)
print(charli.age)
print(miles.species)

#
# Dog('Alex', 22)
# A=Dog('Alex', 22)
# print(A)
#
# buddy = Dog('Buddy', 9)
# miles = Dog('Miles', 4)
# charli = Dog('Charli', 5)
#
# print(buddy.name)
# buddy.age
# print(miles.species)
# buddy.age = 10
# print(buddy.age)
# miles.species = 'Falis silvestris'
# print(miles.species)

# Dog()
# а = Dog()
# b = Dog()
# print(а == b)
