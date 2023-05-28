#Nhập a,b,c
a=float(input("Nhập a= "))
b=float(input("Nhập b= "))
c=float(input("Nhập c= "))
if a==0:
    #Trường hợp pt bậc nhất bx+c=0
    if b==0:
        if c==0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x=-c/b
        print("Phương trình có nghiệm duy nhất x= ",x)
else:
    delta=b**2-4*a*c
    if delta<0:
        print("Phương trinh vô nghiệm ")
    elif delta==0:
        x=(-b)/(2*a)
        print("Phương trình có một nghiệm x=x1=x2 ",x)
    else: #delta >0 --> tính căn delta
        import math
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print("Phương trình có hai nghiệm phân biệt là \n x1= ",x1,"\n x2= ",x2)

