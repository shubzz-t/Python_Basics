
st = "HEY IS UPPER"

low = lambda string: string.lower()

print(low(st))



def return_lambda(x):
    return lambda number: number + x

passing_x=return_lambda(4) #PASING THE value of x to returnn_lambda FUNCTION

passing_x(5)   #PASSING NUMBER VALUE FOR LAMBDA