from random import *
from math import *
from operator import truediv


print(5)
print(-10)
print(3.14)
print('풍선')
print("나비")
print("ㅎ"*8)

print(5 < 10)
print(5 > 10)
print(True)
print(False)
print(not False)
print(not True)
print(not (5 > 10))

'''이것도 주석처리다'''
# 이것도 주석처리다
name = "김딱"
animal = "악어"
age = 4
hobby = "밥먹기"
is_adult = age >= 20

print("우리집" + animal + "가 없어요")
print(name, "은", age, "살이며, ", hobby, "예요")
print(name + "는 어른일까요?" + str(is_adult))

# 퀴즈
station = "사당"
print(str(station) + "행 열차가 들어오고 있습니다.")

# 연산자
print(2**3)  # 2의 3승 = 8
print(5 % 3)  # 나머지 구하기 2
print(10//3)  # 몫 3

print(3 != 5)
print(not(5 > 3))

print((3 > 1) and (2 < 3))
print((3 > 1) & (2 < 3))

print((3 > 1) or (5 < 3))
print((3 > 4) | (2 < 3))

print(5 > 3 > 1)
print(5 > 3 > 5)

print(abs(-5))  # 5
print(pow(4, 2))  # 4의 2승 = 16
print(max(2, 19))  # 19
print(min(3, 30))  # 3
print(round(3.14))  # 반올림 3
print(round(4.8))  # 반올림 5

# 파이썬 수식
#from math import *
print(floor(4.99))  # 내림 4
print(ceil(3.14))  # 올림 4
print(sqrt(16))  # 제곱근 4

# 랜덤 함수
#from random import *
print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10 + 1))  # 1 ~ 10 이하의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성

# 퀴즈
date = randint(4, 28)
print("오프라인 날짜는 매월 " + str(date) + "로 선정되셨습니다")

# 문자열
print('나는 파이썬이')
print("쉬워여")
print("""
나는 파이썬이
쉬워요
""")

# 슬라이싱
jumin = "950123-1234545"

print("성별" + jumin[7])
print("연 : " + jumin[0:2])  # 0 부터 2 직전까지(0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])  # 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])  # 맨 뒤에서 7번째에서 끝까지

# 문자열처리함수
python = "python is woOOOOOow"
print(python.lower())
print(python.upper())
print(python[0].isupper())  # 0 번째 문자를 대문자로
print(len(python))  # 문자열 개수 반환
print(python.replace("python", "Java"))

index = python.index("o")  # "o"가 몇 번째에 있는지
print(index)
index = python.index("o", index + 1)
print(index)

print(python.find("o"))  # 문자가 몇 번째에 있는지
print(python.find("Java"))  # 문자가 없으면 -1 라고 뜬 후, 함수 진행
# print(python.index("Java"))  # 문자가 없으면 에러가 뜨고 종료

print(python.count("n"))  # n이 몇 번 찍히는지
