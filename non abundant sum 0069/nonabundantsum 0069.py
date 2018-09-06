abund=[]
newlist=[]
flag=True
finalsum=0
sum=0

for num in range (1,28123): #checking numbers if abundant and putting in a list
    sum=0
    for z in range(1,num):
        if num%z==0:
            sum=sum+z
            if sum>num:
                abund.append(num)
                break

for n in range(1,28123):
    flag=True
    newlist=[]
    for a in range(0,len(abund)):
        if abund[a] < n:
            newlist.append(abund[a])
        else: #when list has all abundant nos. < n no need to check for rest of abundant nos
            break

    for i in range(0,len(newlist)):
        for j in range(i,len(newlist)):
            abundsum=newlist[i]+newlist[j]
            if abundsum == n: #checks if n is sum of abundant numbers, breaks out of loop if it is
                flag=False
                break
        if flag == False: #breaks out of 2nd nested for loop and n increments
            break
    if flag == True:
        finalsum=finalsum+n
        print(finalsum)
print(finalsum)

#within first 10 minutes it reached finalsum=3million
#totally took about 1 hr 20 min
#only the last 1 mil took 1 hr 10 min the first 3 mil finished in 10 min
#getting list of abundant nos took a minute
#after it printed final answer it took another 45 min to finish running
#means even after the last non abundant sum it had to check for all remaining nos till 28123 and took 45 min
