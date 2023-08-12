# Input marks out of 100 and assign grade as A(90-100), B(70-89), C(50-69) and F(0-49)

a=int(input("Enter marks: "))
if a>=90 and a<=100:
    print("A")
elif a>=70 and a<90:
    print("B")
elif a>=50 and a<69:
    print("C")
else:
    print("D")