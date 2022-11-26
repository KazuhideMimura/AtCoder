# n = int(input())
# n, m = map(int, input().split())
# A = list(map(int, input().split()))

#A
x, y = map(int, input().split('.'))
if y <= 2:
    add = '-'
elif y <= 6:
    add = ''
else:
    add = '+'
print(str(x) + add)

#B
n = int(input())
first, last = [], []
for i in range(n):
    fi, li = input().split()
    first.append(fi)
    last.append(li)

flag = False
for i in range(n):
    for j in range(n):
        if i != j:
            if first[i] == first[j]:
                if last[i] == last[j]:
                    flag = True
                    print('Yes')
                    exit()
if not flag:
    print('No')

#C
n = int(input())
BN = list(bin(n)[2:])
ans = ''
for num in BN:
    if num == '1':
        ans += 'AB'
    else:
        ans += 'B'
ans = ans[:-1]
print(ans)

#D
from collections import OrderedDict
N, M = map(int, input().split())
A = []
colors = {i+1: {} for i in range(N)}
search_dict = OrderedDict()

for m in range(M):
    km = int(input())
    Am = list(map(int, input().split()))
    if len(set(Am)) != km:
        print('No')
        exit()
    else:
        search_dict[m] = Am.pop()
        A.append(Am)

search_dict= sorted(search_dict.items(), key = lambda x:x[1])

def pop_m(pop_list, search_dict, A):
    add_list = []
    for m in pop_list:
        if len(A[m]) >= 1:
            add_list.append(m, A[m].pop())
        else:
            del search_dict[m]
    add_list.sort(key=lambda x:x[1])
    return(search_dict, add_list, A)

# def add(add_list, search_dict):
#     # どちらのリストもソートされていることが前提
#     i, j = 0, 0
#     add_a, add_m = add_list[i]

#     while any([i < len(add_list) - 1, ])


#     for i, ma in enumerate(list(search_dict.items())):
#         if add_value == add_index:
#             pop_list.append()

# 最初の処理：上にあるペアを全て削除
prev_m, prev_a = -1, -1
pop_list = []
for m, a in search_dict:
    if a == prev_a:
        pop_list += [prev_m, m]
    prev_m, prev_a = m, a

search_dict, add_list, A = pop_m(pop_list, search_dict, A)



while(len(search_dict) >= 1):
    pop_list = search(search_dict)
    if len(pop_list) == 0:
        print('No')
        exit()
    else:
        for m1, m2 in pop_list:
            search_dict, A =  pop_m(m1, m2, search_dict, A)
print('Yes')

# #E
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort(reverse=True)
# A += [0]

# score = 0
# k = 0
# i = 0

# while all([i <= N-1, k < K]):
#     a, b = A[i], A[i+1]
#     if a > b:
#         if k + (i+1) * (a - b) <= K:
#             score += (i+1) * (a+b+1)*(a - b)//2
#             k += (i+1) * (a - b)
#         else:
#             j, r = (K-k) // (i+1), (K-k) % (i+1)
#             score += (i+1) * (2*a-j+1) * j // 2 + (a - j) * r
#             k = K
#     i += 1
    
# print(score)