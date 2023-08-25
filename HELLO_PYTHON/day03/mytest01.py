# com = 숫자 맘속에 정하기 1~99 랜덤으로 
# 예)50
from random import random


# 숫자를 맞춰보세요 20
# 20_ (탭)up
# 숫자를 맞춰보세요 20
# 51_ down
# 50 정답입니다
# arr = list(range(1,99+1))



# for i in range(1000):
#     rnd = int(random()*99)
#     a = arr[0]
#     #섞는 방법
#     arr[0] = arr[rnd]
#     arr[rnd] = a
#랜덤숫자
a = int(random()*99)+1
print(a)

while True:
    me = input("숫자를 맞춰보세요")
    menum = int(me)
    if menum>a :
        print(menum,"down")
    elif menum<a:
        print(menum,"up")
    elif menum==a:
        print(menum,"정답입니다")
        break





