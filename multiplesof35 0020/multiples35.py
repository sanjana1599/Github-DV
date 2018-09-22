s=0
for x in range(1000):
  y=x%3
  z=x%5
  if y==0 or z==0:
      s=s+x
print (s)
