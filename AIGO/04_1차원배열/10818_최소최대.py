# https://www.acmicpc.net/problem/10818
# 풀이 아이디어
# - 최솟값은 아주 큰 값, 최댓값은 아주 작은 값으로 시작해서 하나씩 비교하며 갱신
# - 다른 방법: print(min(nums), max(nums))

N = int(input())
nums = list(map(int, input().split()))

mmin = nums[0]    # 첫 번째 값으로 시작하면 초기값 고민이 없다
mmax = nums[0]

for n in nums:
    if n < mmin:
        mmin = n
    if n > mmax:
        mmax = n

print(mmin, mmax)
