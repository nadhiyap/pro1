w=int(input("enter a no of weight"))
v=int(input("enter a no of values"))
l=[]
l1=[]
s=0
for i in range(w):
    a=int(input("enter weight"))
    l.append(a)
    s=s+int(l[i])
print(s)
for i in range(v):
    b=int(input("enter value"))
    l1.append(b)
for i in range(v):
    m=max(l1)
    if(s>=m):
        print(m)
        break
    else:
        l1.remove(max(l1))
        
