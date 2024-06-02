''' 
1. has_key(): We can prevent this by checking whether key is already available or ot by using has_key() function or by using in operator.
'''
d={100: 'a', 200: 'b', 300: 'c'}
# d.has_key(400)

if 400 in d:
    print("Present")
else:
    print("Absent")
    
''' 
2. get(): The get() method returns the value of the item with the specified key.
'''
x=d.get(200)
print(x)

''' 
Add elements to a python dictionary:
1. Using the name of the dictionary with [].
d[key]=value
'''
student_details={100:"abc", 200: "def", 300: "ghi"}
print(student_details)
student_details[400]="jkl"
print(student_details)

''' 
Update Values in Dictionary:
1. We can also use [] to change the value associated witha particular key.
2. If the key is already available then old value will be replaced with new value.
[key]=value
'''
student_details[500]="mno"
print(student_details)
''' 

Delete Elements from the Dictionary
1. del statement can be used to delete an element from the dictionary.
del d[key]
'''
del student_details[500]
print(student_details)

''' 
2. clear(): to remove all entries from the dictionary.
'''
student_details.clear()
print(student_details)

