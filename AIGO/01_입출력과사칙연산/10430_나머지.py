# https://www.acmicpc.net/problem/10430
# 풀이 아이디어
# - 모듈러 성질: (A+B)%C == ((A%C)+(B%C))%C, 곱셈도 동일
# - 큰 수 계산에서 중간중간 나머지를 구해도 결과가 같다는 것을 확인하는 문제

A, B, C = map(int, input().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
