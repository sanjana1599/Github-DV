
x=1
i=1
a=0
flag = True
while flag == True:
    x=x+1
    a=0
    i=1
    while i<21 and a==0:
        s=x%i
        if s!=0:
            a = 1
        elif i==20:
            flag=False
            break
        else:
            i = i + 1
print(x)
