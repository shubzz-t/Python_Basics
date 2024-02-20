#INERITANCE
# SINGLE
# MULTIPLE
# MULTILEVEL

class Car:

    def __init__(self):
        print("ALL CARS ARE BEST")

    def display(self):
        print("WELCOME TO ALL CARS.COM")


class BMW(Car):
    
    def __init__(self):
        print("BMW CARS ARE BEST")

    # def display(self):
    #     print("WELCOME TO BMW.COM")

car1=Car()
b1=BMW()

car1.display()
b1.display()