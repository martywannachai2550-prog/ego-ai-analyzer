m,n= map(int,input().split())

MatrixA=[]
for i in range(m):
    row = list (map(int, input().split()))
    MatrixA.append(row)

MatrixB=[]
for i in range(m):
    row = list(map(int, input().split()))
    MatrixB.append(row)

for i in range(m):
    for j in range(n):
     val = MatrixA[i][j] + MatrixB[i][j]
     print (val, end=" ")
    print()