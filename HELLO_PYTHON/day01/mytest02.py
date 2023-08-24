#홀짝을 선택하시오 input 홀
#나:홀
#컴:홀
#결과: 이김

import random

a= input("홀짝을 선택하세요")
print("나:"+a)

com = random.randint(1, 10)


if com%2==0 :
    com="짝"
elif com%2==1:
    com="홀"
print("컴:"+com)


if a=="홀" and com=="홀":
    print("이김")
elif a=="짝" and com=="짝":
    print("이김")
elif a=="짝" and com=="홀":
    print("졌다")
elif a=="홀" and com=="짝":
    print("졌다")
    




