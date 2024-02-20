# IF ELSE
if (5 < 3):
    print("5 GREATER")
else:
    print("5 SMALLER")


# IF ELIF
if (5 < 3):
    print("5 GREATER")
elif (5 == 5):
    print("5 IS SAME")
else:
    print("5 IS SMALLER")


#NESTED IF
n=6
if(n>4):
    print("n is greater than 4")
    if(n>7):
        print("n is greater than 7 also")



#STRING LENGTH GREATER THAN 10  if else
name=input("ENTER THE NAME:")
if (len(name)>10):
    print("Greater than 10")
else:
    print("less than 10")







#CHECK THAT LIST CONTAINER GIVEN NAME   if else in
names=["abc" , "def" , "ghi" , "jkl"]
name = input("Enter the name")

if name in names:
    print("PRESENT IN LIST")
else:
    print("Not in list")