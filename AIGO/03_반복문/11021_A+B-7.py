# https://www.acmicpc.net/problem/11021
# 풀이 아이디어
# - 케이스 번호가 1부터 시작하므로 range(1, T + 1)

T = int(input())
for case in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'Case #{case}: {A + B}')
