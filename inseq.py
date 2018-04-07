n=int(input("enter a number"))
l=[]
count=1
for i in range(n):
    a=int(input("enter value"))
    l.append(a)
    if l[i-1]==l[i]-1:
        count+=1
print(count)
