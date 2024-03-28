# 영어 월 단어 맞추기 게임
import random # 함수1
month = random.randint(0,11)
month_list = ["January", "February", "March","April", "May", "June", "July", "August", "September", "October", "November", "December"]

x = month_list[month]

msg = "월이 선택되었습니다."
print("{0} {1}".format(month + 1, msg))

user = input("영어단어를 입력하세요.") # 사용자 입력하기

user = user.lower()
x = x.lower()

if x == user:
    print("정답 입니다.")
else:
    print("오답 입니다.")