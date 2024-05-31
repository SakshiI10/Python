from datetime import timedelta

t1=timedelta(days=1)
print("Original timedelta:",t1)

#Multiplication
t2=t1*5.5
print(t2)

#Substraction
t3=t2-t1
print(t3)

#Addition
t3 += t2
print(t3)

#Division
t3=t2/2.5
print(t3)

#floor division
t3=t2//2
print(t3)

#modulo
t3=t2%timedelta(days=3)
print(t3)
