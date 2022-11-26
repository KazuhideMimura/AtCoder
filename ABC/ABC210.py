#A
n, a, x, y = map(int, input().split())
if n <= a:
    ans = x * n
else:
    ans = x * a + y * (n - a)
print(ans)

#B
n = int(input())
S = list(input())
for i, s in enumerate(S):
    if s == '1':
        if i % 2 == 0:
            print('Takahashi')
            break
        else:
            print('Aoki')
            break

#C
n, k = map(int, input().split())
C = list(map(int, input().split()))
count = {}
ans = 0
variation = 0
start = 0

for end in range(n):
    if end - start == k:
        if count[C[start]] == 1:
            del count[C[start]]
            variation -= 1
        else:
            count[C[start]] -= 1
        start += 1
    
    if C[end] in count.keys():
        count[C[end]] += 1
    else:
        count[C[end]] = 1
        variation += 1
    ans = max(ans, variation)
print(ans)

#D
H, W, c = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# for h in range(H):
#     for w in range(W):
#         for d in range(H + W - 2):
            