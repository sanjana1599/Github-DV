a=50000000
b=70000000
flag=True
i=0
while flag == True:
    a1=a+0.03*a
    a=a1
    b1=b+0.02*b
    b=b1
    i=i+1
    if a > b:
        flag=False
print(i)
