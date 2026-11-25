# https://www.acmicpc.net/problem/8393
# 풀이 아이디어
# - 누적합 변수를 0으로 두고 반복하며 더하기
# - 다른 방법: sum(range(1, n + 1)) 또는 공식 n * (n + 1) // 2

n = int(input())

ssum = 0
for i in range(1, n + 1):
    ssum += i

print(ssum)
