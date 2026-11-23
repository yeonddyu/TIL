# https://www.acmicpc.net/problem/11382
# 풀이 아이디어
# - 세 정수 입력도 map + split 으로 한 번에
# - 파이썬 int는 크기 제한이 없어서 큰 수도 그대로 더할 수 있다

A, B, C = map(int, input().split())
print(A + B + C)
