# n = int(input())
# n, m = map(int, input().split())
# A = list(map(int, input().split()))

# A
A = input().split()
if A == sorted(A):
    print('Yes')
else:
    print('No')

#B
tests = ['ABC' , 'ARC', 'AGC', 'AHC']
for _ in range(3):
    tests.remove(input())
print(tests[0])

#C
n = int(input())
P = list(map(int, input().split()))
Q = [0] * n
for i in range(n):
    Q[P[i]-1] = i + 1
print(' '.join(list(map(str, Q))))

#D
from bisect import bisect_left, insort_left
L, Q = map(int, input().split())
cut_points = [0, L]

for q in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        insort_left(cut_points,x)
    else:
        index = bisect_left(cut_points, x)
        print(cut_points[index] - cut_points[index-1])

#E
from collections import deque
import heapq
 
Q1 = deque([])
Q2 = []
heapq.heapify(Q2)
 
N = int(input())
for i in range(N):
    query = input()
    if query[0] == '1':
        x = int(query[2:])
        Q1.append(x)
    elif query[0] == '2':
        if len(Q2) == 0:
            print(Q1.popleft())
        else:
            print(heapq.heappop(Q2))
    else:
        while len(Q1) >= 1:
            heapq.heappush(Q2,Q1.pop())