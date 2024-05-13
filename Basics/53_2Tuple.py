''' 
Q6: Program to get the 4 element from front and 4 element from last of a tuple.
'''
my_tuple=(1,2,3,4,5,6,7,8,9)
fourth_front=my_tuple[3]
fourth_end=my_tuple[-4]
print(fourth_front)
print(fourth_end)

''' 
Q7: Element Check.

element=int(input("Enter an element: "))
if element in my_tuple:
    print(f"{element} exists within the tuple")
else:
    print(f"{element} doesn't exists within the tuple")
'''
    
''' 
Q8: FInding repeated elements in a tuple.
'''
repeated_items=[]
for i in range(len(my_tuple)):
    for j in range(i+1, len(my_tuple)):
        if my_tuple[i]==my_tuple[j] and my_tuple[i] not in repeated_items:
            repeated_items.append(my_tuple[i])
print(f"Repeated items: {repeated_items}")

''' 
Q9: Reversing a tuple.
'''
reversed_tuple=my_tuple[::-1]
print(reversed_tuple)