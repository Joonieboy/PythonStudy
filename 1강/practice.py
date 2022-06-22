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

# 문자열 포맷
# 방법 1
print("나는 %d살입니다." % 20)  # %d는 정수여야 한다.
print("나는 %s를 좋아해요" % "파이썬")  # %s는 문자열이다.
print("Apple은 %c로 시작해요" % 'A')  # %c 는 문자이다.
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))  # 두 가지 문자열 이용법

# 방법 2
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(
    age=20, color="빨간"))  # 변수를 선언하면서 문자열포맷 사용
print("나는 {age}살이며, {color}색을 좋아해요".format(
    color="빨간", age=20))  # 변수를 선언하면서 문자열포맷 사용

# 방법 4 (v3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")  # f를 작성하면, 실제 변수를 사용할 수 있다

# 탈출문자
print("오늘 하루가 너무 즐겁다 \n맞아 참 즐겁다")  # \n 한 칸 아래로
print('저는 "나도코딩"입니다')  # 저는 "나도코딩" 입니다
print("저는 \"나도코딩\"입니다.")  # 저는 "나도코딩" 입니다
# \" \' : 문장 내에서 따옴표

# \\ : 문장 내에서 \
print("C:\\PythonProject")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# 퀴즈 #3
address = "http://naver.com"
my_str = address.replace("http://", "")
my_str = my_str.replace(".com", "")
password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)

url = "http://naver.com"
my_st = url.replace("http://", "")
my_st = my_st[:my_st.index(".")]
# print(my_st)
passworb = my_str[:3] + str(len(my_st)) + str(my_st.count("e")) + "!"
print("{0} 의 비밀번호는 {1}입니다.".format(url, passworb))

bus = ["유재석", "조세호", "박명수"]
print(bus)

# 조세호씨는 몇 번째에 앉아있는가?
print(bus.index("조세호"))

# 하하씨가 다음 정류장에서 다음 자리에 앉았다
bus.append("하하")
print(bus)

# 정형돈씨를 유재석 / 조세호 사이에 태웠다
bus.insert(1, "정형돈")
print(bus)

# 버스에 있는 사람을 한 명씩 뒤에서 꺼냄
print(bus.pop())
print(bus)
# print(bus.pop())
# print(bus)
# print(bus.pop())
# print(bus)
bus.append("유재석")
print(bus)
print(bus.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 3, 9, 6]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형과 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# Dictionary
cabinet = {3: "JaeSeok", 100: "TaeHo"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]) #[]로 했을 때, 값이 없으면 함수 종료
print(cabinet.get(5))  # get으로 하면, 함수종료(X), None이라고 뜸
print(cabinet.get(6), "OK!!")  # 6번에 자료가 없으면, "OK!!"를 준다

print(3 in cabinet)  # True 값이 자료에 있는지 확인
print(5 in cabinet)  # False

cabinet = {"A-3": "JaeSeok", "B-100": "TaeHo"}
print(cabinet["A-3"])
print(cabinet["B-100"])
# New Customer
print(cabinet)
cabinet["A-3"] = "JongKuk"  # 값 변경
cabinet["C-20"] = "SeHo"  # 값 추가
print(cabinet)
# Bye Customer
del cabinet["A-3"]
print(cabinet)

# Print Only Key
print(cabinet.keys())

# Print Only Value
print(cabinet.values())

# Print Key, Value
print(cabinet.items())

# Closed Document
cabinet.clear()
print(cabinet)

# 튜플 / 값 추가 및 변경이 안된다. 무조건 고정된 값
menu = ("Pork", "Beef")
print(menu[0])
print(menu[1])
# menu.add("Fish")

name = ("JongKuK")
age = 20
hobby = "Coding"
print(name, age, hobby)

(name, age, hobby) = ("JaeSeok", 30, "Cook")
print(name, age, hobby)
