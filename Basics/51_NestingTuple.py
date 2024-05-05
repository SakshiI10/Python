# 1) Nesting of Tuple
t1 = (1,2,3,4,5)
t2=('qwerty', 7,8,9)
t3=(t1,t2)
print(t3)

# 2) Nested tuple of only one element
employee=((10,"emp1",13000),)
print(employee)

t4 = ((1,2,3,"hello"), ("world",4,5,6), (7,8,9))
print(t4)
for i in t4:
    for j in i:
        print(j, end="")
    print()
    
# 3) Handling tuple
user_details=('SI', 10, 'BE', 'Pune')
(name, age, education, address)=user_details
print(name)
print(age)
print(education)
print(address)

# 4) Handling tuple using asterisk
''' 
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list.
'''
user_details2=('SI', 10, 'BE', 'Avasari', 'Pune', 'MH')
(name, age, education, *address)=user_details2
print(name)
print(age)
print(education)
print(address)

