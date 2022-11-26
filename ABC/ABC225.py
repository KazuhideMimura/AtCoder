#A
s = len(set(list(input())))
if s == 3:
    print(6)
elif s == 2:
    print(3)
else:
    print(1)

#B
n = int(input())
for i in range(n-1):
    a, b = map(int, input().split())
    if i == 0:
        possible_center = [a, b]
    else:
        if a in possible_center:
            possible_center = [a]
        elif b in possible_center:
            possible_center = [b]
        else:
            possible_center = []
if len(possible_center) == 1:
    print('Yes')
else:
    print('No')

#C
n, m = map(int, input().split())
flag = True
for i in range(n):
    Bi = list(map(int, input().split()))
    # check 1
    if i >= 1:
        if Bi[0] - b_init_prev != 7:
            flag = False
    # check 2
    for j in range(m-1):
        if Bi[j+1] - Bi[j] != 1:
            flag = False
        if Bi[j] % 7 == 0:
            flag = False
    b_init_prev = Bi[0]
    if not flag:
        break
if flag:
    print('Yes')
else:
    print('No')

#D
n, Q = map(int, input().split())
trains = [[i] for i in range(n+1)]
head = [i for i in range(n+1)]
tale = [i for i in range(n+1)]
group = [i for i in range(n+1)]

def print_list(L):
    text = str(len(L))
    for l in L:
        text += (' ' + str(l))
    print(text)

key_num = n + 1
for q in range(Q):
    query = list(map(int, input().split()))
    # print()
    # print(trains)
    # print('head ', head)
    # print('tale ', tale)
    # print('group', group)
    # print(query)

    if query[0] == 1:
        x, y = query[1], query[2]
        new_group = group[x]
        new_head = head[x]
        new_tale = tale[y]
        group_y_prev = group[y]
        for i in trains[group[y]]:
            group[i] = group[x]
            head[i] = new_head
        for i in trains[group[x]]:
            tale[i] = new_tale
        trains[group[x]] += trains[group_y_prev]
        trains[group_y_prev] = []
    
    elif query[0] == 2:
        x, y = query[1], query[2]
        new_groupX = []
        new_groupY = []
        add_to = x
        for i in trains[group[x]]:
            if add_to == x:
                tale[i] = x
                new_groupX.append(i)
            else:
                head[i] = y
                group[i] = key_num
                new_groupY.append(i)
            if i == x:
                add_to = y
        trains[group[x]] = new_groupX
        trains.append(new_groupY)
        key_num +=1

    elif query[0] == 3:
        x = query[1]
        # print(trains[group[x]])
        print_list(trains[group[x]])

#D
n, Q = map(int, input().split())
head = [0] * (n+1)
tale = [0] * (n+1)

def numList2text(L):
    L = list(map(str, L))
    return(' '.join(L))

def query3(x, head = head, tale = tale):
    num = 1
    before = []
    after = []
    search_head = head[x]
    while search_head != 0:
        before.append(search_head)
        search_head = head[search_head]
        num += 1
    before.reverse()

    search_tale = tale[x]
    while search_tale != 0:
        after.append(search_tale)
        search_tale = tale[search_tale]
        num += 1
    trains_list = [num] + before + [x] + after
    print(numList2text(trains_list))


for q in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x, y = query[1], query[2]
        tale[x] = y
        head[y] = x
    
    elif query[0] == 2:
        x, y = query[1], query[2]
        tale[x] = 0
        head[y] = 0

    elif query[0] == 3:
        x = query[1]
        query3(x)