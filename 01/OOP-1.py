class Auto:
    def __init__(self, brand, age, mark, color=None, weight=0):
        self.brand = brand
        self.age = age
        self.mark = mark


    def move(self):
        print("move!")

    def stop(self):
        print("stop!")

    def birthday(self):
        self.age += 1



