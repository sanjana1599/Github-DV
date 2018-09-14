import random
flag=True
count=1
guess=0
print("Enter a limit")
m=int(input())
x=random.randint(1,m)
while flag == True:
    print("Enter your guess")
    guess=int(input())
    if guess > x:
        print("High")
        count=count+1
    elif guess < x:
        print("Low")
        count=count+1
    else:
        print("Correct!")
        flag=False
print(count)
