#com: 1-9 3개를 골라서 만들기()
#com: "325"
# 숫자 3개를 입력하세요 1 2 3 
# 123    1S1B
# 숫자 3개를 입력하세요 3 2 5
# 325 3S0B  정답입니다 !
# 위치는 맞지 않지만 포함된 숫자를 맞추면 볼(Ball)
# 포함된 숫자도 맞고 위치도 맞으면 스트라이크(Strike)






import random #파이썬 랜덤 모듈
correct_number = ["0", "0", "0"] #파이썬에서 input() 함수의 사용자 입력은 문자열이므로 "0" 문자열로 배열
correct_number[0] = str(random.randrange(1, 9+1))
correct_number[1] = str(random.randrange(1, 9+1))
correct_number[2] = str(random.randrange(1, 9+1))


# 랜덤 숫자가 같다면 계속 반복
while(correct_number[0] == correct_number[1]):
    correct_number[1] = str(random.randrange(1, 9+1))
while(correct_number[0] == correct_number[2] or correct_number[1] == correct_number[2]):
    correct_number[2] = str(random.randrange(1, 9+1))


print("정답:",correct_number)

try_number = 0
strike_number = 0
ball_number = 0


print("--------------------------")
while (strike_number < 3):

    number = input("숫자 3자리를 입력하세요: ")

    strike_number = 0
    ball_number = 0

    for i in range(0, 3): # i 값의 범위 0~3
        for j in range(0, 3):
            if(number[i] == str(correct_number[j]) and i == j): # 포함된 숫자도 맞고 위치도 맞으면
                strike_number += 1
            elif(number[i] == str(correct_number[j]) and i != j):# 위치는 맞지 않지만 포함된 숫자를 맞추면 볼
                ball_number += 1
    print("결과: [ {} ]S [ {} ]B".format(strike_number,ball_number))
    try_number += 1

print("--------------------------")
print("결과: [ {} ]S [ {} ]B 정답입니다!!!".format(strike_number,ball_number))
print("[",try_number,"]번 만에 맞췄습니다")
