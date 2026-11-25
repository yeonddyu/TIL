# https://www.acmicpc.net/problem/2439
# 풀이 아이디어
# - 오른쪽 정렬: 공백 (N - i)개 + 별 i개
# - 다른 방법: ('*' * i).rjust(N)

N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)
