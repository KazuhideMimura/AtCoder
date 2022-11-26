# n = int(input())
# n, m = map(int, input().split())
# A = list(map(int, input().split()))

#A
n = int(input())
S = list(input())
if S[n-1] == 'o':
    print('Yes')
else:
    print('No')

#B
P = list(map(int, input().split()))
print(''.join([chr(96 + p) for p in P]))

#C
import numpy as np
n = int(input())
S = np.array([[int(s == '#') for s in list(input())] for _ in range(n)])
T = np.array([[int(t == '#') for t in list(input())] for _ in range(n)])

Sy = np.where(np.sum(S, axis=1) >= 1)[0]
Sy_min, Sy_max = min(Sy), max(Sy)
Sx = np.where(np.sum(S, axis=0) >= 1)[0]
Sx_min, Sx_max = min(Sx), max(Sx)
S1 = S[Sy_min:Sy_max+1, Sx_min:Sx_max+1]

Ty = np.where(np.sum(T, axis=1) >= 1)[0]
Ty_min, Ty_max = min(Ty), max(Ty)
Tx = np.where(np.sum(T, axis=0) >= 1)[0]
Tx_min, Tx_max = min(Tx), max(Tx)
T1 = T[Ty_min:Ty_max+1, Tx_min:Tx_max+1]


flag = False
for i in range(4):
    if S1.shape == T1.shape:
        if np.allclose(S1, T1):
            flag = True
            print('Yes')
            break
    if not flag:
        T1 = np.rot90(T1)

if not flag:
    print('No')


#D
from collections import defaultdict
n = int(input())
XY = []
countX, countY = defaultdict(int), defaultdict(int)
for _ in range(n):
    x, y = map(int, input().split())
    countX[x] += 1
    countY[y] += 1
    XY.append((x, y))

pop_list = []
for i, xy in enumerate(XY):
    x, y = xy
    if any([countX[x] <= 1, countY[y] <= 1]):
        pop_list.append(i)
        countX[x] -= 1
        countY[y] -= 1
XY = [XY[i] for i in range(n) if i not in pop_list]
n -= len(pop_list) 

XY.sort(key = lambda x:x[1])
XY.sort(key = lambda x:x[0])

ans = 0
for i in range(n-2):
    x1, y1 = XY[i]
    mid = []
    for j in range(i+1, n):
        x2, y2 = XY[j]
        if all([x1<x2, y1<y2]):
            if (x1, y2) in mid:
                if (x2, y1) in mid:
                    ans += 1
        mid.append((x2, y2))

print(ans)
