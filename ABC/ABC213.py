# n, a, x, y = map(int, input().split())
# C = list(map(int, input().split()))

#A
a, b = map(int, input().split())
a, b = list(map(int, bin(a)[2:].zfill(8))), list(map(int, bin(b)[2:].zfill(8)))

ans = 0
for i in range(8):
    if a[i] + b[i] == 1:
        ans += 2 ** (7 - i)
print(ans)

#B
n = int(input())
nums = [-1, -2]
ids = [-1, -2]
A = list(map(int, input().split()))

for i, a in enumerate(A):
    if a > nums[1]:
        nums = [nums[1], a]
        ids = [ids[1], i + 1]
    elif a > nums[0]:
        nums = [a, nums[1]]
        ids = [i + 1, ids[1]]
print(ids[0])

#C
h, w, n = map(int, input().split())
A, B = [], []
for i in range(n):
    ai, bi = map(int, input().split())
    A.append(ai)
    B.append(bi)

A_sort, B_sort = sorted(set(A)), sorted(set(B))
A_dict, B_dict = dict(), dict()
for i, a_s in enumerate(A_sort):
    A_dict[a_s] = i
for i, b_s in enumerate(B_sort):
    B_dict[b_s] = i

for i in range(n):
    print(A_dict[A[i]] + 1, B_dict[B[i]] + 1)

#D
n = int(input())
paths = {i:[] for i in range(1, n+1)}
for i in range(n-1):
    ai, bi = map(int, input().split())
    paths[ai].append(bi)
    paths[bi].append(ai)

for i in range(1, n+1):
    paths[i] = sorted(paths[i], reverse=True)

visited = {1:0}
flag1 = True
now = 1
route = ['1']

while flag1:
    flag2 = False
    while len(paths[now]) >= 1:
        next = paths[now].pop()
        if next  != visited[now]:
            route.append(str(next))
            visited[next] = now
            now = next
            flag2 =  True
            break
    
    if not flag2:
        if now == 1:
            flag1 = False
        else:
            now = visited[now]
            route.append(str(now))

print(' '.join(route))

#E
H, W = map(int, input().split())
S = []
for h in range(H):
    S.append(list(input()))

que = [(0, 0, S, 0)] # h, w, S, cnt_break

while len(que) >= 1:
    h, w, S, cnt = que.pop()
    next = []
    if h >= 1:
        next.append(h-1, w)
    if h <= H - 2:
        next.append(h+1, w)
    if w >= 1:
        next.append(h, w-1)
    if w <= W - 2:
        next.append(h, w+1)
