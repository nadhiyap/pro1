n=int(input("enter n"))
l=[]
a=0
for i in range(n):
    a=int(input("enter value"))
    l.append(a)
l.sort()
candy=0
c=1
for i in range(n):
    candy=candy+c
    c=c+1
print(c)
    
