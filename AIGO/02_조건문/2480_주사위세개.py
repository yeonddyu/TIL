# https://www.acmicpc.net/problem/2480
# 풀이 아이디어
# - 세 개 같음 → 두 개 같음 → 모두 다름 순서로 검사 (가장 좁은 조건부터)
# - 두 개가 같을 때는 같은 쪽 눈을 써야 하므로 a가 포함된 경우와 b == c 인 경우를 나눔
# - 모두 다르면 max()로 가장 큰 눈

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + (a * 1000))
elif (a == b) or (a == c):
    print(1000 + (a * 100))
elif b == c:
    print(1000 + (b * 100))
else:
    print(max(a, b, c) * 100)
