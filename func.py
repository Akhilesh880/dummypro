functions 
# syntax 
#def name(arg)
#body of the func



def greet():
	print('hello welcome to python class')
	return '45'

greet()
print(greet())	



======arguments======


1 position argument
2 default argument
3 keyword argument
4 variable length/arbitary argument



------
positional argument
========================


follows the cal by value

def add(a,b):
	print(a+b)
add(1,2)	




 default arguments
-----------------------------


follows the cal by value


def add(a=2,b=5):
	print(a-b)
add(6,4)







=====================
keyword argument
---------------------
follows the cal by reference 

def add(a,b):
	print(a+b)
add(a=1,b=3)	
========================




def deatils(**delt)
	print(delt)


deatils(vineet='india',batman='usa',)

-------------------------------------------------


anaomys func or lambda func
----------      ---------------
lambda ------------- keyword
syntax 


var=lambda arg:expressions------------->function defination
var(parameters)----------------->func call







squ=lambda a:a**2
print(squ(4))


lambda func hav 2 in built func


filter() --------> filter u frm the expression by ur condition
map()----------> map u to obj depending upon ur condition true or false

l=[i for i in range(0,21)]
print(l)+
evn=tuple(map(lambda l: l%2==0,l))
print(evn)
evn=tuple(filter(lambda l: l%2==0,l))
print(evn)



















