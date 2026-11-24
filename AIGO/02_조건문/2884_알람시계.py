# https://www.acmicpc.net/problem/2884
# 풀이 아이디어
# - 분에서 45를 뺐을 때 음수면 60을 더하고 시간을 1 줄임
# - 시간이 음수가 되면(0시 → 전날 23시) 24를 더함
# - 다른 방법: 전체를 분으로 바꿔 계산 → t = (H * 60 + M - 45) % (24 * 60), 출력 t // 60, t % 60

H, M = map(int, input().split())

new_M = M - 45

if new_M < 0:
    M = 60 + new_M
    new_H = H - 1
    if new_H < 0:
        H = 24 + new_H
    else:
        H = new_H
else:
    M = new_M

print(H, M)
