# https://www.acmicpc.net/problem/25304
# 풀이 아이디어
# - 물건 가격 x 개수를 반복하며 누적한 뒤 총액과 비교

X = int(input())
N = int(input())

total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b

if X == total:
    print('Yes')
else:
    print('No')
