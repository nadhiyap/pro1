m=int(input("enter no of rows"))
n=int(input("enter no of cols"))
mat=[n*[0] for i in range(m)]
l=[]
print(mat)
for i in range(m):
    for j in range(n):
        mat[i][j]=int(input())
print(mat)
for r in mat:
    r.sort()
for j in range(n):
    for i in range(m):
        l.append(mat[i][j])
    l.sort()
    for i in range(len(l)):
        mat[i][j]=l[i]
    l.clear()
print(mat)
