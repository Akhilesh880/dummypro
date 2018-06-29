
def cal():
	print('enter 1 for main menu','\n 9 for exit')
cal()	
m=int(input('enter the value'))

if m==1:
	def main():
		print('1 for arithematic operation')
		print('2 for logical operation')
		print('3 for bitwise operation')
		print('4 for relational operation')
		print('5 for membership operation')
		print('6 for assignment operation')
		print('7 for boolean operation')
	
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
					art()
					
					#print('enter the num for operation')
					#x=int(input('enter the value'))
					#if x==1:
					#	return 

					
				elif b==1:
					return main()	
			add()
		elif z==2:
			def sub():
				print('enter the value of c n d')
				c=int(input('enter the value of c   '))
				d=int(input('enter the value of d   '))
				print('the sub of c n d is',c-d)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return art()
				elif b==1:
					return main()	
			sub()
		elif z==3:
			def mul():
				print('enter the value of c n d')
				c=int(input('enter the value of c   '))
				d=int(input('enter the value of d   '))
				print('the mul of c n d is',c*d)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return art()
				elif b==1:
					return main()	
			mul()
		elif z==4:
			def div():
				print('enter the value of c n d')
				c=int(input('enter the value of c   '))
				d=int(input('enter the value of d   '))
				print('the div of c n d is',c/d)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return art()
				elif b==1:
					return main()	
			div()
		elif z==5:
			def mod():
				print('enter the value of c n d')
				c=int(input('enter the value of c   '))
				d=int(input('enter the value of d   '))
				print('the mod of c n d is',c%d)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return art()
				elif b==1:
					return main()	
			mod()			
	elif a==2:
		def log():
			print(' 1 for and')
			print(' 2 for or')
			print(' 3 for not')
		log()
		z=int(input('enter the num for required operation    '))
		if z==1:
			def an():
				print('enter the value of c n d')
				c=int(input('enter the value of c   '))
				d=int(input('enter the value of d   '))
				print('the and of c n d is',c&d)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return log()
				elif b==1:
					return main()	
			an()
		elif z==2:
			def r():
				print('enter the value of c n d')
				c=int(input('enter the value of c   '))
				d=int(input('enter the value of d   '))
				print('the r of c n d is',c/d)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return log()
				elif b==1:
					return main()	
			r()
		elif z==2:
			def nt():
				print('enter the value of c ')
				c=int(input('enter the value of c   '))
			
				print('the nt of c is',~c)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return log()
				elif b==1:
					return main()	
			nt()		

	elif a==3:
		def bit():
			print(' 1 for  bit and')
			print(' 2 for  bit or')
			print(' 3 for  bit not')
		bit()
		z=int(input('enter the num for required operation    '))
		if z==1:
			def btan():
				print('enter the value of c n d')
				c=int(input('enter the value of c   '))
				d=int(input('enter the value of d   '))
				print('the bit and of c n d is',c and d)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return bit()
				elif b==1:
					return main()	
			btan()
		elif z==2:
			def btr():
				print('enter the value of c n d')
				c=int(input('enter the value of c   '))
				d=int(input('enter the value of d   '))
				print('the r of c n d is',c or d)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return bit()
				elif b==1:
					return main()	
			btr()
		elif z==2:
			def btnt():
				print('enter the value of c ')
				c=int(input('enter the value of c   '))
			
				print('the  btnt of c is',~c)
				print('enter 0 for back','\n 1 for main menu')
				b=int(input('enter the value'))
				if b==0:
					return bit()
				elif b==1:
					return main()	
			btnt()	
				