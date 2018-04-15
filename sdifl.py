x=input("enter x")
global x
y=input("enter y")
c=0
for i in range(len(x)):
    d1=ord(x[i])-ord(y[i])
    print(d1)
    c=c+d1
print(c)
