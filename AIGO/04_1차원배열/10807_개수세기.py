# https://www.acmicpc.net/problem/10807
# 풀이 아이디어
# - 리스트를 돌면서 v와 같은 값을 셈
# - 다른 방법: nums.count(v)

N = int(input())
nums = list(map(int, input().split()))
v = int(input())

cnt = 0
for n in nums:
    if n == v:
        cnt += 1

print(cnt)
