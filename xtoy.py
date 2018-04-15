x=input("enter x")
global x
y=input("enter y")
cost=0
def rep():
    global x,y,cost
    if x==y:
        return None
    x=x.replace(x,y)
    cost+=1
    print(x)
rep()
print("x=",x," y=",y)
print(cost)
