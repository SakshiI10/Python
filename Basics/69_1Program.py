# Sorting a dictionary by value
mydict={'abc':1, 'ghi':3,'def':2,'jkl':4,'mno':5}
mykeys=list(mydict.keys())
mykeys.sort()
sorted_dict={i:mydict[i] for i in mykeys}

print(sorted_dict)