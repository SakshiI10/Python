# Add and remove elements in a set.
setF=set()
print(setF)

setF.add("Banana")
print(setF)

setF.update(["Apple", "Chickoo"])
print(setF)

numSet=([1,2,3,4,5])
print("Origignal set: ", numSet)
#numSet.pop()
#print("After pop(): ", numSet)

numSet.discard(3)
print("After discard: ", numSet)

numSet.remove(5)
print(numSet)