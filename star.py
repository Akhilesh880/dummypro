a=int(input('enter a value'))
for i in range(0,a):
	print(a,'|',a+1,'|',a+2)
	a=a+3
	if i==2:
		break
	print('__','__','__')