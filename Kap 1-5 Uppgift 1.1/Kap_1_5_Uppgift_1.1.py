a1 = int(input("A="))
b1 = int(input("B="))
c1 = int(input("C="))

if a1<b1 and b1<c1:
    print("False")
elif a1<b1:
    print("True")
elif b1<c1:
    print("True")
else:
    print("a is bigger than b and b is bigger than c")
