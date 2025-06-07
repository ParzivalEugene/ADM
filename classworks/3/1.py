def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y


def mod_inverse(a, m):
    gcd_val, x, _ = extended_gcd(a, m)
    if gcd_val != 1:
        return None
    return (x % m + m) % m


def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


N = 33
p, q = 3, 11
phi_N = (p - 1) * (q - 1)

print(f"N = {N} = {p} × {q}")
print(f"φ(N) = {phi_N}")

e = None
d = None
for e_candidate in range(2, phi_N):
    if gcd(e_candidate, phi_N) == 1:
        d_candidate = mod_inverse(e_candidate, phi_N)
        if d_candidate is not None:
            e = e_candidate
            d = d_candidate
            print(f"e = {e}, d = {d}")
            break

if e is not None and d is not None:
    m = 7
    c = pow(m, e, N)
    m_decrypted = pow(c, d, N)

    print(f"Сообщение: {m}")
    print(f"Зашифровано: {c}")
    print(f"Расшифровано: {m_decrypted}")
