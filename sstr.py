string=input("enter the str")
substr=input("enter the sub string")
if substr in string:
    print(substr)
else:
    print(substr[1::])
