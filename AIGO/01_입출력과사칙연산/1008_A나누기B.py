# https://www.acmicpc.net/problem/1008
# 풀이 아이디어
# - / 는 정수끼리 나눠도 실수를 반환 (오차 범위 내면 그대로 출력해도 정답)

A, B = map(int, input().split())
print(A / B)
