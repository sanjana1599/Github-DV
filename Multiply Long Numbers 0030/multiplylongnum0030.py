mid=0
c=-1
zr=""
z="0"
prod=0
a=""
print("Enter two numbers to be multiplied")
n1=int(input())
n2=int(input())
if n2 > n1:
    mid=n1
    n1=n2
    n2=mid #larger num is n1, smaller is n2
while n2 > 0:
    last=n2%10 #last digit
    full=n2//10 #the number without the last digit
    a1=n1*last
    c=c+1
    if c > 0:
        zr=zr+z #adding zeroes behind the product
    a=str(a1)+zr
    prod=prod+int(a)
    n2=full
print(prod)
