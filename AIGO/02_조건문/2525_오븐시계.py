# https://www.acmicpc.net/problem/2525
# 풀이 아이디어
# - 분을 먼저 더한 뒤 // 60 은 시간으로 올리고, % 60 은 남은 분
# - 시간이 24 이상이면 다음 날이므로 24를 뺌
# - 입력 범위상 하루 넘게 넘어가지 않지만, (A + B // 60) % 24 로 쓰면 더 안전하다

A, B = map(int, input().split())
C = int(input())

ssum = B + C
new_A = A + (ssum // 60)
new_B = ssum % 60

if new_A >= 24:
    print(new_A - 24, new_B)
else:
    print(new_A, new_B)
