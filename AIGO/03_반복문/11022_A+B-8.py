# https://www.acmicpc.net/problem/11022
# 풀이 아이디어
# - 11021번과 같고 출력 형식만 다름 → f-string에 A, B도 넣기

T = int(input())
for case in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'Case #{case}: {A} + {B} = {A + B}')
