# https://www.acmicpc.net/problem/25314
# 풀이 아이디어
# - 4바이트마다 long 하나 → N // 4 번 반복
# - 문자열 * 정수로 반복 문자열을 만들 수 있다

N = int(input())

cnt = N // 4
print('long ' * cnt + 'int')
