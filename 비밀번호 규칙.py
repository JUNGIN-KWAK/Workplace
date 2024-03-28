# 홈페이지 비밀번호 만들기
url = input()
my_str = url.replace("http://", "") # 규칙1
print(my_str)

my_str = my_str[:my_str.index(".")] # 규칙2 my_str[0:5] 0~5 직전까지 잘림
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url,password))