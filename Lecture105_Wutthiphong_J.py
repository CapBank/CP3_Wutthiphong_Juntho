class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAir(self):
        print("Trun on air")

class Car(Vehicle):
    pass

class Van(Vehicle):
    pass

class Pickup(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnOnAir()
van1 = Van()
van1.turnOnAir()
pickup1 = Pickup()
pickup1.turnOnAir()
estatecar1 = Estatecar()
estatecar1.turnOnAir()