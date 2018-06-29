
a=[[5,4],[6,7]]
b=[[1,2],[3,4]]
print(a[0])
print(a[1])
print(b[0])
print(b[1])





result = [[a[i][i] * b[i][i] + a[i][j] * b[j][i]  for j in range(len(a))] for i in range(len(a)) ]
  
for r in result:
    print(r)