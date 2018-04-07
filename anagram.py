s=input("enter a string")
a=input("enter a string")
l=[]
l1=[]
for i in range(len(s)):
    l.append(s[i])
for j in range(len(a)):
    l1.append(a[j])
l.sort()
l1.sort()
print(l)
print(l1)
if l==l1:
    print("yes")
else:
    print("no")
