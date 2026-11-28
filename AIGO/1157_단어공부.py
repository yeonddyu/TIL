# https://www.acmicpc.net/problem/1157
# 풀이 아이디어
# - 대소문자를 구분하지 않으므로 upper()로 전부 대문자로 통일
# - 알파벳 26칸짜리 리스트(bucket)에 개수를 셈: ord(문자) - ord('A') 가 인덱스
# - 최댓값과 그 위치를 찾고, 최댓값이 2개 이상이면 '?' 출력

word = input()
new_word = word.upper()

bucket = [0] * 26

for w in new_word:
    idx = ord(w) - 65
    bucket[idx] += 1

mmax = bucket[0]
mmax_idx = 0
for i in range(len(bucket)):
    if bucket[i] > mmax:
        mmax = bucket[i]
        mmax_idx = i

cnt = 0
for b in bucket:
    if b == mmax:
        cnt += 1

if cnt > 1:
    print('?')
else:
    print(chr(65 + mmax_idx))


# ------------------------------------------------------------
# [다른 풀이 1] 내장 함수 max, count, index 사용
# - 최댓값 찾기와 개수 세기를 반복문 대신 리스트 메서드로 처리
# ------------------------------------------------------------
# word = input().upper()
#
# bucket = [0] * 26
# for w in word:
#     bucket[ord(w) - ord('A')] += 1
#
# mmax = max(bucket)
# if bucket.count(mmax) > 1:
#     print('?')
# else:
#     print(chr(bucket.index(mmax) + ord('A')))


# ------------------------------------------------------------
# [다른 풀이 2] 딕셔너리로 개수 세기
# - 단어에 실제로 나온 알파벳만 키로 저장
# - dict.get(키, 0): 키가 없으면 0을 기본값으로 사용
# ------------------------------------------------------------
# word = input().upper()
#
# count = {}
# for w in word:
#     count[w] = count.get(w, 0) + 1
#
# mmax = max(count.values())
# candidates = [k for k, v in count.items() if v == mmax]
#
# if len(candidates) > 1:
#     print('?')
# else:
#     print(candidates[0])


# ------------------------------------------------------------
# [다른 풀이 3] collections.Counter 사용
# - Counter: 각 원소의 개수를 세어 주는 딕셔너리
# - most_common(2): 가장 많이 나온 것부터 2개를 (원소, 개수) 형태로 반환
# - 1등과 2등의 개수가 같으면 최댓값이 여러 개
# ------------------------------------------------------------
# from collections import Counter
#
# word = input().upper()
# top = Counter(word).most_common(2)
#
# if len(top) > 1 and top[0][1] == top[1][1]:
#     print('?')
# else:
#     print(top[0][0])
