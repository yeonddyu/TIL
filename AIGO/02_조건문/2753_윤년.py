# https://www.acmicpc.net/problem/2753
# 풀이 아이디어
# - 윤년: (4의 배수이면서 100의 배수가 아님) 또는 400의 배수
# - 두 조건을 or로 묶으면 한 번에 검사할 수 있다

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)
