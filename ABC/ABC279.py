# A
S = list(input())
ans = 0
for s in S:
    if s == 'v':
        ans += 1
    else:
        ans += 2
print(ans)

# B
s = input()
t = input()
if t in s:
    print('Yes')
else:
    print('No')

# C
# AC65, WA5, TLE4
# python
import numpy as np
h, w = map(int, input().split())
# 転置された入力を取得
S, T = [], []
for i in range(h):
    S.append([s == '#' for s in list(input())])
for i in range(h):
    T.append([t == '#' for t in list(input())])
S = np.array(S).T.astype(int)
T = np.array(T).T.astype(int)

S2, T2 = set(), set()
for i in range(w):
    S2.add(''.join(list(map(str, list(S[i])))))
    T2.add(''.join(list(map(str, list(T[i])))))

if S2 == T2:
    print('Yes')
else:
    print('No')

# C
# AC65, WA5, TLE4
h, w = map(int, input().split())
# S の転置を取得
for i in range(h):
    if i == 0:
        S = list(input())
    else:
        Si = list(input())
        S = [S[j] + Si[j] for j in range(w)]
# T の転置を取得
for i in range(h):
    if i == 0:
        T = list(input())
    else:
        Ti = list(input())
        T = [T[j] + Ti[j] for j in range(w)]
if set(S) == set(T):
    print('Yes')
else:
    print('No')

# C
# AC
# 参考：https://atcoder.jp/contests/abc279/submissions/36828380
h, w = map(int,input().split())
S = [input() for _ in range(h)]
T = [input() for _ in range(h)]
St = list(zip(*S))
Tt = list(zip(*T))
if sorted(St) == sorted(Tt):
    print('Yes')
else:
    print('No')

# D
a, b = map(int, input().split())
# 試行回数を x とするとき，dtdx = b - a/2 * (1+x) ** (-3/2)
if b - a/2 >= 0:
    # 微分が常に正 --> 単調増加 --> x = 0 で最小
    ans = a
else:
    x = (a / (2 * b)) ** (2/3) - 1
    # [x] - 1, [x], [x] + 1 の場合を調べればよい
    check_list = [int(x) -1, int(x), int(x) + 1]
    check_list = [cl for cl in check_list if cl >= 0] # 0 以上に限定
    for i, ix in enumerate(check_list):
        fx = b * (ix) + a * (1 + ix) ** (-1/2)
        if i == 0:
            ans = fx
        else:
            ans = min(ans, fx)
print(ans)
