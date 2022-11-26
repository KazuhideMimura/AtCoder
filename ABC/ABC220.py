# A
a, b, c = map(int, input().split())

if a % c == 0:
    print(a)
else:
    candidate = c * (a // c + 1)
    if candidate <= b:
        print(candidate)
    else:
        print(-1)

#B
k = int(input())
A, B = input().split()
A, B = list(A), list(B)

def base10(A, k):
    num = 0
    order = 1
    for a in reversed(A):
        num += order * int(a)
        order *= k
    return(num)

print(base10(A, k) * base10(B, k))

#C
n = int(input())
A = list(map(int, input().split()))
x = int(input())

count = len(A) * (x // sum(A)) 
rest = x % sum(A)

flag = False
for a in A:
    rest -= a
    count += 1
    if rest < 0:
        flag = True
        break

if not flag:
    for a in A:
        rest -= a
        count += 1
        if rest < 0:
            flag = True
            break

print(count)

#D
n = int(input())
A = list(map(int, input().split()))
large = 998244353

now = [0] * 10
now[A[0]] += 1

for i in range(1, len(A)):
    new = [0] * 10
    for j in range(10):
        if now[j] >= 1:
            f = (j + A[i]) % 10
            g = (j * A[i]) % 10
            new[f] = (new[f] + now[j]) % large
            new[g] = (new[g] + now[j]) % large
    now = new

for i in range(10):
    print(now[i])

#E
n, d = map(int, input().split())
large = 998244353
ans = 0

num = 1
A = [0] * (max(n, d // 2) + 1)
for i in range((max(n, d // 2) + 1)):
    A[i] = num
    num = (num * 2) % large

for a in range(d):
    b = d - a
    if b < a:
        break
    if b <= n - 1:
        top = A[n-b] - 1
        if a == 0:
            bottom_1 = 1
        else:
            bottom_1 = A[a-1]
        bottom_2 = A[b-1]
            
        if a == b:
            add = (2 * top * bottom_1) % large
        else:
            add = (4 * top * bottom_1) % large
        add = (add * bottom_2) % large
        ans = (add + ans) % large

print(ans)