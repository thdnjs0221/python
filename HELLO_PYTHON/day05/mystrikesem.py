#com: 1-9 3개를 골라서 만들기()
#com: "325"
# 숫자 3개를 입력하세요 1 2 3 
# 123    1S1B
# 숫자 3개를 입력하세요 3 2 5
# 325 3S0B  정답입니다 !
# 위치는 맞지 않지만 포함된 숫자를 맞추면 볼(Ball)
# 포함된 숫자도 맞고 위치도 맞으면 스트라이크(Strike)
from random import random

def randCom():
    arr=[1,2,3,4,5,6,7,8,9]
    for i in range (100):
        rnd = int(random()*9)
        
        a= arr[0]
        arr[0]=arr[rnd]
        arr[rnd]=a
        
         
    return "{}{}{}".format(arr[0],arr[1],arr[2])
def getS(mine,com):
    cnt=0
    m1=mine[0:1]
    m2=mine[1:2]
    m3=mine[2:3]
    
    c1=com[0:1]
    c2=com[1:2]
    c3=com[2:3]
    
    if m1==c1 : cnt+=1
    if m2==c2 : cnt+=1
    if m3==c3 : cnt+=1
    return cnt


def getB(mine,com):
    cnt=0
    m1=mine[0:1]
    m2=mine[1:2]
    m3=mine[2:3]
    
    c1=com[0:1]
    c2=com[1:2]
    c3=com[2:3]
    
    if m1==c2 or m1==c3: cnt+=1
    if m2==c1 or m2==c3: cnt+=1
    if m3==c1 or m3==c2: cnt+=1
    return cnt

com = randCom()
print("com",com)
while True:
    mine = input("숫자 3개를 입력하세요")
    s= getS(mine,com)
    b= getB(mine,com)
    if s==3:
        print("{}\t{}s{}b\t정답입니다".format(mine,s,b))
        break;
    else:
        print("{}\t{}s{}b".format(mine,s,b))
    