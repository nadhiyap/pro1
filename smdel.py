a=int(input("enter a"))
n=int(input("enter n"))
b=str(a)
l=[]
for i in range(len(b)):
    l.append(b[i])
for i in range(n,len(b)):
        print(int(l[i]),end=' ')
