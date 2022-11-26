# B
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt1 = 0
for i in range(n):
    if A[i] == B[i]:
        cnt1 += 1
print(cnt1)

A.sort()
B.sort()
ai, bi = 0, 0
cnt2 = 0

while all([ai < n, bi < n]):
    if A[ai] == B[bi]:
        cnt2 += 1
        ai += 1
        bi += 1
    elif A[ai] > B[bi]:
        bi += 1
    else:
        ai += 1
print(cnt2 - cnt1)
 
# C
n = int(input())
XYS = []
for _ in range(n):
    x, y = map(int, input().split())
    XYS.append([x, y])
S = [int(s == 'R') for s in list(input())]
for i in range(n):
    XYS[i].append(S[i])

XYS.sort(key = lambda x:x[0])
XYS.sort(key = lambda x:x[1])

i = 0
flag = False
while i <= n - 2:
    if XYS[i][2] == 0:
        i += 1
    else:
        y = XYS[i][1]
        j = 1
        
        while True:
            if i + j >= n:
                i += j
                break
            elif XYS[i+j][1] == y:
                if XYS[i+j][2] == 0:
                    print('Yes')
                    flag = True
                    i = n + 1
                    break
                else:
                    j += 1
            else:
                i += j
                break
if not flag:
    print('No')

#D
n, x = map(int, input().split())
S = list(input())
new_S = []
cnt_lr = 0
for s in S:
    if cnt_lr == 0:
        new_S.append(s)
        if s != 'U':
            cnt_lr += 1
    else:
        if s == 'U':
            new_S.pop()
            cnt_lr -= 1
        else:
            new_S.append(s)
            cnt_lr += 1

for s in new_S:
    if s == 'U':
        x //= 2
    elif s == 'L':
        x *= 2
    else:
        x = 2 * x + 1
print(x)
