def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


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


def prime_factorization(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def count_coprime_bruteforce(n):
    count = 0
    coprimes = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
            coprimes.append(i)
    return count, coprimes


N = 143

print(f"Задача 4: Подсчет количества чисел меньших и взаимно простых с N = {N}")
print()


factors = prime_factorization(N)
print(f"Разложение {N} на простые множители: {factors}")


print(f"{N} = {factors[0]} × {factors[1]}")
print()


phi_n = euler_totient(N)
print(f"φ({N}) = {phi_n}")


p, q = 11, 13
phi_formula = (p - 1) * (q - 1)
print(
    f"Проверка формулой: φ({p}×{q}) = ({p}-1) × ({q}-1) = {p - 1} × {q - 1} = {phi_formula}"
)
print()


count_brute, coprime_list = count_coprime_bruteforce(N)
print(f"Проверка перебором: количество = {count_brute}")
print(f"Первые 20 взаимно простых чисел с {N}: {coprime_list[:20]}")
print(f"Последние 10 взаимно простых чисел с {N}: {coprime_list[-10:]}")

print(f"\nОтвет: Количество чисел меньших {N} и взаимно простых с ним равно {phi_n}")
