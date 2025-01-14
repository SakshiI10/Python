''' 
1. disjoint(): Returns whether two sets have a intersection or not.

2. issubset(): Returns whether another set contains this set or not.

3. issuperset(): Returns whether this set contains another set or not.

4. union(): Return a set containing the union of sets.

5. copy(): Returns a copy of the set.
'''

x={"bat", "ball", "stump"}
y={"cat", "bat", "rat"}
z=x.symmetric_difference(y)
print(z)
print("After intersection method: ",x)
x.intersection_update(y)
print("after intersection_update method: ", x)

z=x.isdisjoint(y)
z1=x.issubset(y)
z2=x.issuperset(y)
print(z)
print(z1)
print(z2)