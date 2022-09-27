import random

def f(x):
    return pow(x,2)+pow(x,3)

q=10000000
s=2*1
cnt=0
for i in range (q):
    x=random.random()
    y=random.uniform(0,2)
    if f(x)>y:
        cnt+=1
print (cnt*s/q)