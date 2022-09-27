import random
def f(x):
    return pow(x,2)-2
#二分查找法
min = 0
max = 2
x=(min+max)/2
d=0.0001
while abs(f(x))>d:
    if f(x)>0:
        max=x
    else:
        min=x
    x=(min+max)/2
print(x)
#牛顿法
x=1
while abs(f(x))>d:
    x=(x+2/x)/2
print (x)
#蒙特卡罗法
def g(x):
    return pow(x,0.5)
q=100000
cnt=0
s=2*2
for i in range (q):
    x=random.uniform(0,2)
    y=random.uniform(0,2)
    if g(x)>y:
        cnt+=1
print(s*3*cnt/(q*4))
