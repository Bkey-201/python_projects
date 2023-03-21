class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
            self.name = name
            self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriver(Dog):
    def speak(self, sound="Tyaf"):
        return f"{self.name} barks {sound}"

charlie = GoldenRetriver("charlie", 5)

print(charlie.speak())