#TO FIND THE SIZE OF A TEXT FILE IN BYTES
def size_finder():
    a=input("Enter The Text File Name : ")
    x=open(a,'r')
    y=x.read()
    print("The size of the text file is ",len(y))
    x.close()
size_finder()
