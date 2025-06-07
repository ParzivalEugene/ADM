def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N = 2867
p, q = 47, 61
phi_N = (p - 1) * (q - 1)

print(f"N = {N} = {p} × {q}")
print(f"φ(N) = {phi_N}")

for e in range(2, phi_N):
    if gcd(e, phi_N) == 1:
        print(f"Наименьшее e = {e}")
        break
