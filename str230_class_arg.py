# class Gqw:
#     def kl(self,age,name):
#         self.age=age
#         self.name=name
#
# Sd=Gqw(1,'22')
# Sd.name

class Cats:
    def init(self, name, age):
        self.name = name
        self. age = age
# Метод экземпляра
    def description(self):
        return f"{self.name} is {self.age} years old"
# Другой метод экземпляра
    def speak(self, sound):
        return f"{self.name} says {sound}"

# miles=Cats('Rt', 11)

class B:
    n = 5
    def adder(v):
        return v + B.n

B.n

B.adder(4)
print(B.adder(4))


class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the car
        """
        return "%s braking" % self.vtype

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving a %s %s!" % (self.color, self.vtype)


if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())