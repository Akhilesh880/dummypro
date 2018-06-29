a=(1,'hello',45.7,8+9j)
for i in a:
	print(i,end='  ')
print(a.count(1))
print(a.index(1))	
print(a)
a=(i for i in range(*0,11))
#print(a)
#generates object and object is a
for i in a:
	print(i)
print(next(a))	





enumerator objects



enumerate()      consists of index num and value
a=('batman','iron msn','supermanb')
enum=list(enumerate(a))
print(enum)
print(next(enum))
print(next(enum))
for i in enum:
	print(i)




inbuilt functions

all()
any()
sum()
min()
max()
enumerate()
len()
tuple()
list()




l=[1,2,(4,5),78]
t=(2,3,4,[22,45,56],46)
l[2][0]='am changed'
print(l)
