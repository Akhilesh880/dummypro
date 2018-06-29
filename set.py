a={1,'hello',(45,43,2),56+0j,[4,5,6]}
print(a)
print(type(a))



# accesing
print(a)
a.update([1,2,3,4])
a.add(56)
print(a)
a={i for i in range(0,10,2)}
print(a)
b={i for i in range(0,10,3)}
print(b)
a.pop()
#a.popitem()
a.clear()
#print(a+b)
print(a-b)



print(a.symmetric_difference(b))






#  unionn
-----------------------------------


a={i for i in range(0,10,2)}
print(a)
b={i for i in range(0,10,3)}
print(b)



print(a|b)
print(a.union(b))
print(a&b)
print(a.intersection(b))







a={1,2,3,4,5}
b={1,2,3}
print(a.issubset(b))
print(a.issuperset(b))







pritn(len(a))
print(sum(a))
print(min(a))
print(max(a))
print(enumerate(a))
b=




frozen set       
