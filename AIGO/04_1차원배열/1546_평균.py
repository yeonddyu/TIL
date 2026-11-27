# https://www.acmicpc.net/problem/1546
# 풀이 아이디어
# - 최댓값 M을 먼저 구한 뒤, 모든 점수를 (점수 / M * 100)으로 바꿔서 평균
# - 다른 방법: 식을 정리하면 sum(nums) / M * 100 / N 으로 반복문 없이 계산 가능

N = int(input())
nums = list(map(int, input().split()))
mmax = max(nums)

ssum = 0
for n in nums:
    ssum += ((n / mmax) * 100)

print(ssum / N)
