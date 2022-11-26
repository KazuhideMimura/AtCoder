#A
s, t, x = map(int, input().split())
flag = True
now = s
while True:
    if now == t:
        print('No')
        break
    elif now == x:
        print('Yes')
        break
    else:
        if now <= 23:
            now += 1
        else:
            now = 0

#B
n, x = map(int, input().split())
A = list(map(int, input().split()))
know = [0] * n
now = x-1
while True:
    know[now] = 1
    next = A[now] - 1
    if know[next] == 1:
        break
    else:
        now = next
print(sum(know))

#C
n, k = map(int, input().split())
scores = [sum(list(map(int, input().split()))) for _ in range(n)]
boder = sorted(scores, reverse=True)[k-1]
for s in scores:
    if s >= boder - 300:
        print('Yes')
    else:
        print('No')

#D
# union find
# https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.next_blank = [i for i in range(n)]
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
        nb_new = max(self.next_blank[x], self.next_blank[y])
        self.next_blank[x] = nb_new
        self.next_blank[y] = nb_new
    def update_ub(self, x):
        pass
        

q = int(input())
n = 2 ** 20
A = [-1] * n
uf = UnionFind(n)
for _ in range(q):
    t, x = map(int, input().split())
    index = x % n
    if t == 1:
        index = uf.get_nb(index)
        A[index] = x
        uf.union(index, index)
        
        if A[index + 1] != 1:
            uf.union(index, index + 1)
        if A[index - 1] != 1:
            uf.union(index, index - 1)

    else:
        print(A[index])