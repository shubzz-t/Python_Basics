class Car:
    company="BMW"

    def __init__(self):
        print("CREATED THE OBJECT")

    @staticmethod
    def disp():
        print("THIS IS THE BEST MODEL")

car1=Car()
Car.disp()