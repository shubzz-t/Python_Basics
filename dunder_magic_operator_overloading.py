class magic:

    def __init__(self , num):
        print("created obj")
        self.num=num

    def __add__(self,num2):       # __add__() is default method for operator overloading
        print("ADDING")
        return self.num+num2.num
    
    def __str__(self):
        return f"Number is : {self.num}"
    

n1=magic(4)
n2=magic(6)

sum= n1 + n2
sum= n1 + n2
print(sum)

n4= magic(5)
print(n4)


# for __mul__(self)  --> for multiplication
# for __sub__(self)  --> for subtration
# for __truediv__(self)  --> for x/y
# for __str__(self) --> for fstring
