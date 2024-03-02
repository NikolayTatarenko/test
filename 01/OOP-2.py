import time

class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight


    def move(self):
        print("move!")

    def stop(self):
        print("stop!")

    def birthday(self):
        self.age += 1



class Truck(Auto):

    def __init__(self,brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark,color,weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print("attention")


    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):

    def __init__(self,brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


truck_1 = Truck(brand="Volvo", age=5, mark="XC", max_load=2000)
truck_2 = Truck(brand="Mercedes", age=2, mark="GLA", max_load=3000)

truck_1.move()
truck_2.load()

car_1 = Car(brand="Toyota", age=2, mark="Camry", max_speed=220)
car_2 = Car(brand="BMW", age=1, mark="X5", max_speed=250)

car_1.move()
car_2.move()