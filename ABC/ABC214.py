# n, a, x, y = map(int, input().split())
# C = list(map(int, input().split()))

# A
n = int(input())
if n <= 125:
    print(4)
elif n <= 211:
    print(6)
else:
    print(8)

#B
s, t= map(int, input().split())
ans = 0
for a in range(s + 1):
    for b in range(s + 1):
        for c in range(s + 1):
            if all([a + b + c <= s, a * b * c <= t]):
                ans += 1
print(ans)

# C
# 方針：全ての宝石が i=1 に到達する時刻を求める
# --> ans(i+1) = min(ans(i) + S[i], T[i])
n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

sum_s = 0
for i in range(n):
    if i == 0:
        ans_0 = T[i]
    else:
        sum_s += S[-i]
        ans_0 = min(ans_0, T[-i] + sum_s)

for i in range(n):
    if i == 0:
        ans = ans_0
    else:
        ans = min(T[i], ans + S[i-1])
    print(ans)

#D
n = int(input())
nodes = []
for i in range(n-1):
    u, v, w = map(int, input().split())
    nodes.append ((u-1, v-1, w)) # 頂点は 0 始まりで格納
nodes.sort(key=lambda x:x[2])

# union_find
# https://note.nkmk.me/python-union-find/
from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

uf = UnionFind(n)
ans = 0
for u, v, w in nodes:
    ans += w * (uf.size(u) * uf.size(v))
    uf.union(u, v)
print(ans)

#E
def solve(n, L, R):
    flag = True
    key_points = sorted(set(L + R))
    for i, min in enumerate(key_points):
        l_included = [min <= l for l in L]
        for max in key_points[i:]:
            r_included = [r <= max for r in R]
            cnt = sum([l_included[j] * r_included[j] for j in range(n)]) 
            if cnt > (max - min + 1):
                flag = False
    if flag:
        print('Yes')
    else:
        print('No')

T = int(input())
for t in range(T - 1):
    n = int(input())
    L, R = [], []
    for i in range(n):
        li, ri = map(int, input().split())
        L.append(li)
        R.append(ri)
    solve(n, L, R)
