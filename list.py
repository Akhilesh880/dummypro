l=[1,2,3,'hello',45.4,67+9j]
print(l)
print(type(l))
print(type(l[0]),type(l[3]),type(l[4]),type(l[5]))
l1=[1,2,3,'hello',45.4,67+j]
l2=[4,5,6]
c=l1+l2
print(c)
del c[0]
c.pop()
c.pop()
print(c)
print(l1)
l1.append(2)
print(l1)
l1.insert(3,l2)
print(l1)
print(2*l1)
print(l1[0])
l1[0]='iam replaced'
print(l1)
a='digitallync'
print(list(a))

l=[i for i in range(0,11)]
print(l)
s=[a for a in 'digitallync']
print(s)
a=['hello','welcome',34,[23,45,67]]
print(a[1][1])
print(a[3][2])
a=[i for i in range (0,11)]
print(a)
for l in a:
	print(l)
print(sum(a))
print(min(a))
print(max(a))
a=[0,1,2,3,4,5,6]
print(all(a))
print(any(a))
	
