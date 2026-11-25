# https://www.acmicpc.net/problem/2739
# 풀이 아이디어
# - range(1, 10)으로 1~9까지 반복, f-string으로 출력 형식 맞추기

N = int(input())

for i in range(1, 10):
    print(f'{N} * {i} = {N * i}')
