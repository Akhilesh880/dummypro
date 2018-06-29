a = [[6,2],[5,2]]
	
b = [[5,2],[3,2]]
r = [[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):

        for k in range(len(b)):
            r[i][j] += a[i][k] * b[k][j]	
for r in r:
    print(r)