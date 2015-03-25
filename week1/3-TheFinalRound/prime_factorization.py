def prime_factorization(n):
    i = 2
    factors = {}

    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            if not i in factors.keys():
                factors[i] = 1
            else:
                factors[i] += 1

    if n > 1:
        if not n in factors.keys():
            factors[n] = 1
        else:
            factors[n] += 1

    return sorted(zip(factors.keys(), factors.values()), key=lambda x: x[0])

if __name__ == '__main__':
    print(prime_factorization(356))


