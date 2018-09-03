i=1
sum=0
lis=[]
a=2
sum1=0
def amicable(x): #function to find factors of a number
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum=sum+i
    return sum

while a < 10000:
    num1=amicable(a) #eg a is 220, num1=284
    num2=amicable(num1) #then num1 ie 284 is put to the test to see if its amicable to 220
    if num2==a and num1 not in lis and num1!=num2: #to check for amicable, to make sure we're not repeating this check, & to remove pairs like 6 and 6 
        lis.append(a)
        lis.append(num1)
        sum1=sum1+a+num1
    a=a+1

print(sum1)
