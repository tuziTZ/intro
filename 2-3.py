import random
q=100000
#arctan1
x=0
for i in range(q):
    x+=pow(-1,i)/(2*i+1)
print(x*4)
#Fouier级数
x=0
for i in range(q):
    x+=1/(pow(2*i+1, 2))
print(pow(x*8,0.5))
#蒙特卡罗法
def g(x):
    return pow(1-x*x,0.5)
cnt=0
for i in range (q):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    if g(x)>y:
        cnt+=1
print(cnt*4/(q))
#迭代相同次数，方法2的精度最高，其次方法1，精度最低的是方法3
