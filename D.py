# 標準入力を受け付ける。
S = input()

K = int(input())

N = len(S)

# Sのある番目の文字が登場した時に、左から.の文字が何回出現したのかメモする変数。
cnt_dot = []
for _ in range(N + 1):
    cnt_dot.append(0)

for i in range(N):
    if S[i] == '.':
        cnt_dot[i + 1] += cnt_dot[i] + 1
    else:
        cnt_dot[i + 1] += cnt_dot[i]

ans = 0
r = 0
for l in range(N):
    # .の数がKよりも少ない間まで、rの更新を行う。
    while r < N and cnt_dot[r + 1] - cnt_dot[l] <= K:
        r += 1
    ans = max(ans, r - l)

print(ans)
