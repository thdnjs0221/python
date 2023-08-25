# 가위바위보를 선택하세요 가위
#나: 가위
#컴: 랜덤으로  가위
#결과: 비김
from random import random

a = input("가위바위보를 선택하세요:")
b = random()
# print(b)
result ="";
if b>0.66:
    com="가위"
elif b>0.33:
    com="바위"
else :
    com="보"  
    
if a=="가위" and com=="가위":
    result="비김"
elif a=="가위" and com=="바위":
    result="졌음"
elif a=="가위" and com=="보":
    result="이김"
elif a=="바위" and com=="가위":
    result="이김"
elif a=="바위" and com=="바위":
    result="비김"
elif a=="바위" and com=="보":
    result="졌음"
elif a=="보" and com=="보":
    result="비김"
elif a=="보" and com=="가위":
    result="졌음"
elif a=="보" and com=="바위":
    result="이김"
print(a)
print(com)
print(result)
     