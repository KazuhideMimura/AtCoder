#C
from math import factorial

S, k = input().split()
S, k = sorted(list(S), reverse=True), int(k)
n = len(S)

# 文字数をカウントする辞書を作る
cnt_letters = {}
for s in S:
    if s not in cnt_letters.keys():
        cnt_letters[s] = 1
    else:
        cnt_letters[s] += 1

def count_rest(cnt_letters):
    # 残りの文字列で何通り作れるか
    num = factorial(sum(list(cnt_letters.values())))
    if num >= 0:
        for v in cnt_letters.values():
            num //= factorial(v)
    return(num)

cnt = 0
que = [('', cnt_letters)]
while len(que) >= 1:
    text, cnt_letters = que.pop()
    if len(text) == n:
        cnt += 1
        if cnt == k:
            print(text)
            exit()
    else:
        if cnt + count_rest(cnt_letters) < k:
            cnt += count_rest(cnt_letters)
        else:
            for l in cnt_letters.keys():
                if cnt_letters[l] >= 1:
                    new_cnt = cnt_letters.copy()
                    new_cnt[l] -= 1
                    que.append((text + l, new_cnt))

# # D
n, m = map(int, input().split())
A = list(map(int, input().split()))

# 素数列挙
def sieve_eratosthenes(n):
    if n <= 3:
        is_prime = [0, 0, 1, 1][:n+1]
    else:
        # 偶数を除外することで高速化する
        if n % 2 == 0:
            is_prime = [0, 0, 1, 1] + [0, 1] * (n // 2 - 2) + [0]
        else:
            is_prime = [0, 0, 1, 1] + [0, 1] * (n // 2 - 1)
        for p in range(3, int(n ** 0.5) + 1, 2):
            if is_prime[p]:
                for q in range(p * p, n + 1, 2 * p):
                    is_prime[q] = 0
    primes = [i for i in range(n + 1) if is_prime[i]]
    return(primes)

# この問題に必要な素数列
primes = sieve_eratosthenes(max(max(A), m))

# 素因数分解，因数だけ求める
def get_factors(n, primes):
    factors = []
    if n != 1:
        for p in primes:
            if p <= int(n ** 0.5 + 1):
                if n % p == 0:
                    factors.append(p)
                    while n % p == 0:
                        n //= p
            else:
                break
        if n != 1:
            factors.append(n)
    return(factors)

# A に含まれる数の因数をチェックする
prime_checked = {p:0 for p in primes}
for a in A:
    for f in get_factors(a, primes):
        prime_checked[f] = 1

# 1~m までの数から，Aの因数の定数倍を除外する
answers = [0] + [1] * (m)
for p, checked in prime_checked.items():
    if checked:
        for i in range(1, m // p + 1):
            answers[p * i] = 0

print(sum(answers))
for i in range(m + 1):
    if answers[i] == 1:
        print(i)