# 標準入力を受けつける。
A, B = map(str, input().split())

# A, Bの数字を確認して、桁数の少ない数字に対して、0埋めを行う。
# 参考 : https://note.nkmk.me/python-zero-padding/
if len(A) > len(B):
    B = B.zfill(len(A))

# A, Bの数字を確認して、桁数の少ない数字に対して、0埋めを行う。
# 参考 : https://note.nkmk.me/python-zero-padding/
if len(B) > len(A):
    A = A.zfill(len(B))

N = len(A)
for i in range(N):
    a = int(A[N - i - 1])
    b = int(B[N - i - 1])

    # A, Bの数字の各桁を足し合わせて10以上になるかどうか確認する。10以上になる場合、Hard, そうでない場合Easyと出力する。
    if a + b >= 10:
        print('Hard')
        exit()

print('Easy')
