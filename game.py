def main(a):
	print('\n')
	for i in range(3):
		print('__',a,'|','__',a+1,'|','__',a+2)
		a=a+3
	print('     |', '     |')	
print(main(1))	