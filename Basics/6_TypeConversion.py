''' 
Type Conversion:
1) It is the process of converting value of one data type to another compatible data type.
2) Python supports 2 type of type conversion:
    i) Implicit type conversion
    ii) Explicit type conversion
i) Implicit type conversion:
a) This is done mechanically and implicitly by Python.
b) While converting, it is necessary to take care to avoid data loss and hence python promotes conversion from lower data type to higher data type from integer float.
'''
a=5
b=1.234
c=a+b
print(c)

''' 
ii) Explicit type conversion:
a) We know that Python is object oriented.
b) Hence Python allows user to convert data type of an object to required data type.
c) Python supports explicit type conversion using predefined funstion int(), float(), str(), etc.
d) Explicit type conversionis also called as Type Casting
'''
a=125
b=254.25
c="23"
d="135.69"
sum1=a+int(c)
print(sum1)

sum2=b+float(d)
print(sum2)

s1=11
s2="22"
s3=str(s1)+s2
print(s3)