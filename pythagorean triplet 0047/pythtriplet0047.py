import math
for i in range(1,1001):
    for j in range(i+1,1001):
        p=(i**2)+(j**2)
        k=math.sqrt(p)
        if (k).is_integer() == True:
            if i+j+k == 1000:
                print(i," ",j," ",int(k))
                print(int(i*j*k))
