# https://www.acmicpc.net/problem/14681
# 풀이 아이디어
# - x의 부호로 먼저 나누고, 그 안에서 y의 부호로 다시 나누는 중첩 if
# - 입력이 한 줄에 하나씩 들어오므로 input()을 두 번 사용

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
