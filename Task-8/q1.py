import numpy as np 

First = int(input("First Number: "))
second = int(input("Last Number: "))

arr= np. arange(First, (second+1))
print (arr)
res = []
for i in arr:
    res.append(i)
    for j in range(5):
        res.append(0)
for k in range(5):
    res.pop()
print(res)