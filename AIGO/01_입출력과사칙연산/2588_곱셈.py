# https://www.acmicpc.net/problem/2588
# 풀이 아이디어
# - 두 번째 수를 문자열로 받아 인덱스로 각 자릿수를 꺼냄
# - 인덱스 [2]가 일의 자리, [1]이 십의 자리, [0]이 백의 자리
# - 마지막 값은 세 줄을 자릿값만큼 더한 것 = num1 * int(num2)

num1 = int(input())
num2 = input()

print(num1 * int(num2[2]))   # 일의 자리
print(num1 * int(num2[1]))   # 십의 자리
print(num1 * int(num2[0]))   # 백의 자리
print(num1 * int(num2))      # 전체 곱
