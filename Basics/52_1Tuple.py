''' 
Q1: Create a list of tuples with the first element as the number and second element as the square of the number.
'''
my_lists=[1, 2, 3, 4, 5]
my_tuple_list=[(num, num**2) for num in my_lists]
print(my_tuple_list)

''' 
Q2: Create a tuple with numbers and print one item.
'''
my_tuple=(1,2,3,4,5)
print(my_tuple[2])

''' 
Q3: Unpack a tuple in several variables.
'''
my_tuple2=6,7,8
print(my_tuple2)
n1,n2,n3=my_tuple2
print(n1+n2+n2)
#n1,n2,n3,n4=my_tuple2

''' 
Q4: Program to add an Item in a Tuple.
'''
new_tuple=my_tuple+(6,)
print(new_tuple)

''' 
Q5: Creating a tuple to a string.
'''
my_string=''.join(map(str,my_tuple))
print(my_string)