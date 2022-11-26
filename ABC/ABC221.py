# a, b, c = map(int, input().split())
# n = int(input())
# A = list(map(int, input().split()))

#A
a, b = map(int, input().split())
print(32 ** (a - b))

#B
A = list(input())
B = list(input())

C = [A[i] != B[i] for i in range(len(A))]
if sum(C) == 0:
    ans = 'Yes'
elif any([sum(C) >= 3, sum(C) == 1]):
    ans = 'No'
else:
    change1, change2 = [i for i in range(len(A)) if C[i]]
    change2 = change1 + 1
    B_ = B[:change1] + [B[change2]] + B[change1+1:change2] + [B[change1]] + B[change2+1:]
    if A == B_:
        ans = 'Yes'
    else:
        ans = 'No'

print(ans)

#C
def list2num(A):
    A.reverse()
    num = 0
    order = 1
    for a in A:
        num += a * order
        order *= 10
    return(num)
N = list(map(int, list(input())))
N.sort(reverse=True)
ans = 0
for i in range(2 ** len(N)):
    a = list(map(int, list(bin(i)[2:].zfill(len(N)))))

    A = [N[i] for i in range(len(N)) if a[i]]
    B = [N[i] for i in range(len(N)) if a[i] == 0]
    if all([len(A) >= 1, len(B)>= 1]):
        if all([A[0] >= 1, B[0] >= 1]):
            ans = max(ans, list2num(A) * list2num(B))
print(ans)

#D
n = int(input())
A, B = [], []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(a + b)
    
day_flow = {i:0 for i in sorted(list(set(A + B)))}
for a in A:
    day_flow[a] += 1
for b in B:
    day_flow[b] -= 1

ans = [0] * (n + 1)
cnt = 0
for k, v in day_flow.items():
    if cnt == 0:
        memory = v
        day_prev = k
    else:
        ans[memory] += k - day_prev
        memory += v
        day_prev = k
    cnt += 1

ans = list(map(str, ans))
print(' '.join(ans[1:]))

#E
n = int(input())
A = list(map(int, input().split()))
large = 998244353

# 2^n (mod large) を求めておく
seconds = []
num = 1
for i in range(n):
    seconds.append(num)
    num = num * 2 % large

ans = [0] * n
for i in range(n - 1):
    for j in range(i + 1, n):
        if A[i] <= A[j]:
            ans[j-i-1] += 1

            #ans = (ans + seconds[(j-i-1)]) % large
num = 0
for i, a in enumerate(ans):
    num = (num + seconds[i] * a) % large
print(ans)