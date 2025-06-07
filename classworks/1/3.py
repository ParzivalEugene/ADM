def to_mixed_sys(n, m, q):
    n = int(str(n), m)
    res = ""
    for i in q:
        res += str(n % i)
        n //= i
    res += str(n)
    return res[::-1]


print(to_mixed_sys(317, 8, (8, 4, 2)))
