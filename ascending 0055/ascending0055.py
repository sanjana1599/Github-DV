lis=[]
print("Enter list of numbers")
inp=input()
lis1=inp.split()
for a in lis1:
    lis.append(int(a))
count=0
count1=0
j=0

for i in range(len(lis)-1):
    j=i+1
    if lis[i] < lis[j]:
        count=count+1
    else:
        count1=count1+1
if count == (len(lis)-1):
    print("Ascending")
elif count1 == (len(lis)-1):
    print("Descending")
else:
    print("None")
