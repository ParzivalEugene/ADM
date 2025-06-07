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


N = 2867
p, q = 47, 61
e = 11
phi_N = (p - 1) * (q - 1)

d = mod_inverse(e, phi_N)

print(f"N = {N}, e = {e}")
print(f"φ(N) = {phi_N}")
print(f"d = {d}")

if d is not None:
    encrypted = 615
    decrypted = pow(encrypted, d, N)

    print(f"Зашифрованное сообщение: {encrypted}")
    print(f"Расшифрованное сообщение: {decrypted}")
