def main():
	print('1 for arithematic operation')
	print('2 for logical operation')
	print('3 for bitwise operation')
	print('4 for relational operation')
	print('5 for membership operation')
	print('6 for assignment operation')
	print('7 for boolean operation')
	print('8 for main menu')
	print('9 for exit')
main()
a=int(input('enter num for required operation    '))
if a==1:
	def art():
		print(' 1 for add')
		print(' 2 for sub')
		print(' 3 for mul')
		print(' 4 for div')
		print(' 5 for mod')
	art()	
	z=int(input('enter the num for required operation    '))
	if z==1:
		def add():
			print('enter the value of c n d')
			c=int(input('enter the value of c   '))
			d=int(input('enter the value of d   '))
			print('the add of c n d is',c+d)
			print('enter 0 for back','\n 1 for main menu')
			b=int(input('enter the value'))
			if b==0:
				return art()
			elif b==1:
				return main()	
		add()
	elif z==2:
		def sub():
			print('enter the value of c n d')
			c=int(input('enter the value of c   '))
			d=int(input('enter the value of d   '))
			print('the sub of c n d is',c-d)
			return art()
		sub()
	elif z==2:
		def mul():
			print('enter the value of c n d')
			c=int(input('enter the value of c   '))
			d=int(input('enter the value of d   '))
			print('the mul of c n d is',c*d)
			return art()
		mul()
	elif z==4:
		def div():
			print('enter the value of c n d')
			c=int(input('enter the value of c   '))
			d=int(input('enter the value of d   '))
			print('the div of c n d is',c/d)
			return art()
		div()
	elif z==5:
		def mod():
			print('enter the value of c n d')
			c=int(input('enter the value of c   '))
			d=int(input('enter the value of d   '))
			print('the mod of c n d is',c%d)
			return art()
		mod()			

			
































#def add(c,d):
#			print('enter the values of c n d')
#			c=int(input('enter the value of c'))
#			d=int(input('enter the value of d'))

#			print(c+d)
#	    add()    
	#elif b==2:
	#	def sub(c,d):
	#		print(c-d)
	#	sub()	
		#	return art()