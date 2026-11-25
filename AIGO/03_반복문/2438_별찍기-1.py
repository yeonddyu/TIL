# https://www.acmicpc.net/problem/2438
# 풀이 아이디어
# - i번째 줄에 별 i개 → '*' * i

N = int(input())
for i in range(1, N + 1):
    print('*' * i)
