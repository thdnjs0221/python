# 출력할 단수를 입력하세요 5
# 5*1 = 5
# 5*5 = 10
# 5*9 = 45

a = input("출력할 단수를 입력하세요")
aa = int(a)

for i in range(1,9+1):
    print("{}*{} {}".format(aa,i,aa*i))



# for i in range(1,aa+1):
#     print()

