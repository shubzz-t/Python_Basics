class Car:
    company="BMW"

    def __init__(self, name , age):
        self.name=name
        self.age=age
        
    def disp(self):
        print(f"THE COMPANY IS {self.company}")
        
        
car1=Car("Shubham", 23)  # Car.disp(car1)
print(car1.name)
print(car1.age)
car1.company="Mercedes"
car1.disp()
        
    




    