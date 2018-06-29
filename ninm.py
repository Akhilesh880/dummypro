x=[[0,0],[0,0]]
y=[[0,0],[0,0]]
print('the elements of x')
for i in range (len(x)):
	for j in range (len(x[0])):
		
		x[i][j]=int(input(x[i][j]))
		print('enter the next element')
print('x=',x)
print('the elements of y')		


for i in range (len(y)):
	for j in range (len(y[0])):
		
		y[i][j]=int(input(y[i][j]))	
		print('enter the next element')	
print('y=',y)
r = [[x[i][j] + y[i][j]  for j in range(len(x[0]))] for i in range(len(x))]
print('the sum is')  
for r in r:
    print(r)
#for i in range(len(x)):
 #   for j in range(len(y[0])):

  #      for k in range(len(y)):
   #         m[i][j] += x[i][k] * y[k][j]	
m += [[[ x[i][k] * y[k][j] for k in range(y)] for j in range(len(y[0]))] for i in range(len(x))]            
print('the multiplication is')            
for m in m:
    print(m)    