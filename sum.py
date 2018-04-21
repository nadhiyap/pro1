n=int(input("enter n"))
k=int(input("enter n"))
l=[]
b=0
c=0
for i in range(n):
    b=int(input("enter value"))
    l.append(b)
print(l)
for i in range(n):
    if i==n-1:
        break
    else:
        if l[i]+l[i+1]==k:
            c=0
            break
        else:
            c=1
if c==0:
    print("yes")
else:
    print("no")
