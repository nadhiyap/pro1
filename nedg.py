n=int(input("enter no of nodes"))
e=int(input("enter no of edges"))
v=0
v1=0
l=[]
c=0
for i in range(e):
    u=int(input("enter value u"))
    v=int(input("enter value v"))
    if u==v1:
        print(s,',',u,',',v)
        c=s+u+v
    else:
        print(u,',',v)
        c=u+v
    l.append(c)
    s=u
    v1=v
print(max(l))
