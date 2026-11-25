# https://www.acmicpc.net/problem/15552
# 풀이 아이디어
# - 입력이 많을 때 input()은 느리므로 sys.stdin.readline() 사용
# - readline()은 끝에 줄바꿈(\n)이 붙지만 int()와 split()이 알아서 처리한다

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
