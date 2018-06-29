b={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
c=input('enter the value')
a=1
#
for i in range(0,3):
	for i in range(0,10):
		if (c==i):
			d=(a,a+1,a+2)
			a=a+3
	if i==2:
		break
	print(a,'--+','--+','--')


