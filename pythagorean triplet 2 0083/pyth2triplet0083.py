import math
print("Enter 3 numbers")
a1=int(input())
b1=int(input())
c1=int(input())
if a1 < b1:
    if a1 < c1:
        a=a1
        if b1 < c1:
            b=b1
            c=c1
        else:
            b=c1
            c=b1
    else:
        b=a1
        if b1 < c1:
            a=b1
            c=c1
        else:
            a=c1
            c=b1
elif b1 < c1:
    a=b1
    if a1 < c1:
        b=a1
        c=c1
    else:
        b=c1
        c=a1
else:
    b=b1
    if a1 < c1:
        a=a1
        c=c1
    else:
        a=c1
        c=a1

p=(a**2)+(b**2)
x=math.sqrt(p)
if x == c:
    print("TRUE")
else:
    print("FALSE")
