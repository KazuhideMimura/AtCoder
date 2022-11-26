# n = int(input())
# a, b, c = map(int, input().split())
# A = list(map(int, input().split()))

#A
n, k, a = map(int, input().split())
for _ in range(k-1):
    if a < n:
        a += 1
    elif a == n:
        a = 1
print(a)

#B
n = int(input())
S = list(map(int, input().split()))
cnt = 0

for s in S:
    flag = False
    for a in range(1, 150):
        b = round((s-3*a) / (4*a + 3), 8)
        if all([b >= 1, b == int(b)]):
            flag = True
            break
    if not flag:
        cnt += 1
print(cnt)

#C
from math import floor
n = int(input())
ans = 0
for a in range(1, floor(round(n ** (1/3), 9)) + 1):
    n_a = n/a
    for b in range(a, floor(round(n_a ** (1/2), 9)) + 1):
        ans += floor(n_a/ b) - b + 1
print(ans)

#D
n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
A.sort(reverse=True)

ans += A[k] - A[k+1]
