MOD = 998244353

def mobius(n):
    mu = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i, n + 1, i):
                is_prime[j] = False
                mu[j] *= -1
            for j in range(i * i, n + 1, i * i):
                mu[j] = 0
    return mu

def solve(n, m):
    mu = mobius(m)
    result = 0
    for d in range(1, m + 1):
        count = pow(m // d, n, MOD)
        result = (result + mu[d] * count) % MOD
    return result
