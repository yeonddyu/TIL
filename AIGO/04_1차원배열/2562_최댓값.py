# https://www.acmicpc.net/problem/2562
# 풀이 아이디어
# - 최댓값을 갱신할 때 그 위치(인덱스)도 idx에 같이 저장
# - 출력은 반복 변수 i가 아니라 저장해 둔 idx
# - 문제는 몇 번째 수인지(1부터)를 묻기 때문에 idx + 1

mmax = -21e8
idx = 0
for i in range(9):
    n = int(input())
    if n >= mmax:
        mmax = n
        idx = i

print(mmax)
print(idx + 1)
