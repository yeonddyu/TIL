# https://www.acmicpc.net/problem/1330
# 풀이 아이디어
# - 크다 / 작다 / 같다 세 경우를 if-elif-else로 나눔

A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
