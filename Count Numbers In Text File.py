#TO COUNT THE NUMBERS PRESENT IN THE TEXT FILE
def count_number():
    a=input("Enter The Text File Name : ")
    x=open(a,'r')
    y=x.read()
    count=0
    for i in y:
        if i.isdigit()==True:
            count+=1
    print("The Total Numbers Present in this Text File is ",count)
count_number()
