# https://www.acmicpc.net/problem/10950
# 풀이 아이디어
# - 첫 줄의 테스트 케이스 수 T만큼 반복하며 입력받기
# - 반복 변수를 쓰지 않을 때는 _ 로 표시

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)
