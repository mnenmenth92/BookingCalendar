class Vehicle():
    def __init__(self, num_of_wheels):
        self.num_of_wheels = num_of_wheels

    def print_wheels_num(self):
        print(self.num_of_wheels)

class Car(Vehicle):
    pass

smax = Car(4)
smax.print_wheels_num()