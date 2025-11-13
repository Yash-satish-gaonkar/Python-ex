class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Doors: {self.num_doors}")

car = Car("Toyota", "Corolla", 4)
car.display()
