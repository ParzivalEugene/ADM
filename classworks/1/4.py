def to_mixed_sys(n, m, q):
    n = int(str(n), m)
    res = []
    for i in q:
        res.append(str(n % i))
        n //= i
    res.append(str(n))
    return res[::-1]


print(to_mixed_sys(38712, 10, (60, 60, 24, 7)))
