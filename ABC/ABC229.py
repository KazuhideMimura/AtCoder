#A
S1 = input()
S2 = input()

if S1 == "##":
    print('Yes')
elif S1 == "..":
    print('Yes')
elif S1 == "#.":
    if S2 in ['##', '#.', '..']:
        print('Yes')
    else:
        print('No')
elif S1 == '.#':
    if S2 in ['##', '.#', '..']:
        print('Yes')
    else:
        print('No')

#B
A, B = input().split()
A = list(reversed(list(A)))
B = list(reversed(list(B)))

max_i = min(len(A), len(B))
ans = 'Easy'
for i in range(max_i):
    a, b = int(A[i]), int(B[i])
    if a +  b >= 10:
        ans = 'Hard'
print(ans)

#C
import numpy as np
n, w = map(int, input().split())
A, B = [], []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ranks = np.argsort(A)[::-1]

score = 0
for r in ranks:
    a, b = A[r], B[r]
    if w >= b:
        score += a * b
        w -= b
    elif w > 0:
        score += a * w
        w = 0
print(score)

#D
S = list(input())
S = [int(s == 'X') for s in S]
k = int(input())
