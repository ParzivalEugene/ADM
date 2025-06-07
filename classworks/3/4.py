def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_period(a, N):
    current = a % N
    for r in range(1, N):
        if current == 1:
            return r
        current = (current * a) % N
    return None


def euler_totient_bruteforce(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count


a = 4
N = 2491

period = find_period(a, N)
phi_N = euler_totient_bruteforce(N)

print(f"a = {a}, N = {N}")
print(f"Период функции f(x) = {a}^x mod {N}: r = {period}")
print(f"φ({N}) = {phi_N}")

if period is not None:
    print(f"Отношение φ(N)/r = {phi_N}/{period} = {phi_N // period}")
    if phi_N % period == 0:
        print("φ(N) делится на r")
    else:
        print("φ(N) не делится на r")
