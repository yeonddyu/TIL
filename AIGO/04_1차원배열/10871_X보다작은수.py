# https://www.acmicpc.net/problem/10871
# 풀이 아이디어
# - 조건에 맞는 값만 새 리스트에 append
# - print(*리스트): 리스트를 풀어서 공백으로 구분해 출력

N, X = map(int, input().split())
arrA = list(map(int, input().split()))

ans = []
for a in arrA:
    if a < X:
        ans.append(a)

print(*ans)
