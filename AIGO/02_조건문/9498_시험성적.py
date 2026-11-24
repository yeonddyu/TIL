# https://www.acmicpc.net/problem/9498
# 풀이 아이디어
# - 높은 점수부터 검사하면 elif에서 아래 범위(< 90 등)를 다시 쓸 필요가 없다

score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
