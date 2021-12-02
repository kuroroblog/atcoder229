# 標準入力を受け付ける。
N, W = map(int, input().split())

data = []
for _ in range(N):
    A, B = map(int, input().split())
    data.append((A, B))

# N種類のチーズを、1[g]あたりのおいしさが、大きい順に並べ替える。
data.sort(reverse=True)

ans = 0
for d in data:
    # チーズの重さの合計を超える場合。
    if W - d[1] < 0:
        ans += (d[0] * W)
        break
    # チーズの重さの合計を超えていない場合。
    else:
        W -= d[1]
        ans += (d[0] * d[1])

print(ans)
