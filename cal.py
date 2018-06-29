print('hi welcome enter 1 for menu')
a=int(input('enter the value'))
if a==1:
	y=print('enter the value','\n 1 for arithematic','\n 2 for logical','\n 3 for relational','\n 4 for bitwise','\n 5 for membership','\n 6 for assignment','\n 7 for boolean')
b=int(input('enter the value'))
if b==1:
	x=print('enter the value','\n 1 for addition','\n 2 for sub','\n 3 for mul','\n 4 for div','\n 5 for modulo')
	c=int(input('enter the value'))
	if c==1:
		print('enter the values of a n b')
		d=int(input('enter the value of a '))
		e=int(input('enter the value of b '))
		f=d+e
		print('the addition of a n b is',f)
		print('enter 0 for main menu','1 ')
		#z=int(input('enter 0 for main menu ','enter 1 for back'))
		z=int(input('enter the value'))
		if z==0:
			print(y)
		elif z==1:	
			print(x)

	elif c==2:
		print('enter the values of a n b')
		d=int(input('enter the value of a '))
		e=int(input('enter the value of b '))
		f=d-e
		print('the sub of a n b is',f)	
	elif c==3:
		print('enter the values of a n b')
		d=int(input('enter the value of a '))
		e=int(input('enter the value of b '))
		f=d*e
		print('the mul of a n b is',f)	
	elif c==4:
		print('enter the values of a n b')
		d=int(input('enter the value of a '))
		e=int(input('enter the value of b '))
		f=d/e
		print('the  div of a n b is',f)			
	elif c==5:
		print('enter the values of a n b')
		d=int(input('enter the value of a '))
		e=int(input('enter the value of b '))
		f=d%e
		print('the sub of a n b is',f)
elif b==2:
	print('enter the value ','\n 1 for logical and ','\n 2 for logical or','\n 3 for logical not')	
	c=int(input('enter the value'))
	if c==1:
		print('enter the values of a n b')
		d=int(input('enter the value of a '))
		e=int(input('enter the value of b '))
		f=d&e
		print('the logical and of a n b is',f)
	elif c==2:
		print('enter the values of a n b')
		d=int(input('enter the value of a '))
		e=int(input('enter the value of b '))
		f=d|e
		print('the logiacl or of a n b is',f)	
	elif c==3:
		print('enter the values of a ')
		d=int(input('enter the value of a '))
		f= ~d
		print('the logical not of a is',f)			
					
