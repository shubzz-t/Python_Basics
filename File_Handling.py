#FILE HANDLING
#MODES OF FILE TO READ r,w,a,t
#rb read in binary mode
#rt read in text mode

f = open("shubham.txt","r")
data=f.read()
print(data)
f.close()



f = open("shubham.txt","r")
data=f.readline()
print(data)
f.close()




#WRITING TO FILE
f=open("myfile.txt","w")
f.write("Please wrtie this data to file")
f.close()




#APPENDING TO FILE
f=open("myfile.txt","a")
f.write("Now please append the data to file")
f.close()




# FILE HANDLING WITH STATEMENT no need of closing file explicitely
with open("shubham.txt" , "r") as f:
    a=f.read()
    print(a)
