# n = int(input())
# a, b, c = map(int, input().split())
# A = list(map(int, input().split()))

#A
n = input()
print(n.zfill(4))

#B
p= int(input().split()[-1])
print(sum([int(a)<p for a in input().split()]))

#C
from collections import OrderedDict
n, m = map(int, input().split())
A = [list(input()) for _ in range(2 * n)]
win = OrderedDict({i:0 for i in range(2 * n)})

def janken(hand1, hand2):
    """
    hand: G or C or P
    return: 0: even, 1: 1 is winner, 2: 2 is winner
    """
    num1 = ['G', 'C', 'P'].index(hand1)
    num2 = ['G', 'C', 'P'].index(hand2)
    if num1 == num2:
        return(0)
    elif num1 - num2 in [-1, 2]:
        return(1)
    else:
        return(2)

for round in range(m):
    key_num = 0
    for game in range(n):
        k1 = list(win.keys())[key_num]
        hand1 = A[k1][round]
        key_num += 1
        
        k2 = list(win.keys())[key_num]
        hand2 = A[k2][round]
        key_num += 1
        
        result = janken(hand1, hand2)
        if result == 1:
            win[k1] += 1
        elif result == 2:
            win[k2] += 1

    win = OrderedDict(sorted(win.items(), key=lambda x: x[0]))
    win = OrderedDict(sorted(win.items(), key=lambda x: x[1], reverse=True))

for k in win.keys():
    print(k + 1)

        
#D
from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
large = 998244353

prev = defaultdict(int)
prev[-1] = 1 # initialize

for i in range(n):
    k_min, k_max = min(prev.keys()), max(prev.keys())
    
    now = defaultdict(int)
    a, b = A[i], B[i]
    if a <= b:
        for j in range(a, b + 1):
            if k_min > j:
                pass
            elif j <= k_max:
                now[j] = prev[j]
            else:
                now[j] = prev[k_max]

    prev = defaultdict(int)
    num = 0
    for k, v in now.items():
        num = (num + v) % large
        prev[k] = num

ans = 0
for cnt in now.values():
    ans = (ans + cnt) % large
print(ans)

#E

large = 998244353