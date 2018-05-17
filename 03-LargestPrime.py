factors = []
def prime_factors(n):
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return factors

print(prime_factors(600851475143))
print(max(factors))