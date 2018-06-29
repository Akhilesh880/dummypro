a=[[5,4],[6,7]]
b=[[1,2],[3,4]]
#print(a[i][j]+b[i][j])
#for i in i range (0,2,1):
	#for j in j range (0,2,1)
	#print(a[i][j]+b[i][j])
#for a[i][j] in a range():
	#for b[i][j] in a range():
		#print(a[i][j]+b[i][j])
#i+,j+
#result=[[0,0][0,0]]
#for i in range(len(a)):
 
   # iterate through columns
 #  for j in range(len(a[0])):
  #     result[i][j] = a[i][j] + b[i][j]
  
#for r in result:
 #    print(r)
result = [[a[i][j] + b[i][j]  for j in range(len(a[0]))] for i in range(len(a))]
  
for r in result:
    print(r)