print("숫자게임 시이작")
number = 62
# input()은 값을 입력받는 함수
exact_num = input("1에서 100사이 숫자 추측해라")
# 문자열로 넘어온 값을 int()로 숫자로 바꾼다
guess = int(exact_num)
if guess == number:
    print("맞았으")
else:
    print("틀렸으")

print("게임종료")
