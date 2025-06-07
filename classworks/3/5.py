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


a = 7
N = 187

print(f"N = {N}, a = {a}")

period = find_period(a, N)
print(f"Период функции f(x) = {a}^x mod {N}: r = {period}")

if period is not None and period % 2 == 0:
    print(f"Период четный: r = {period}")

    x = pow(a, period // 2, N)
    print(f"a^(r/2) mod N = {a}^{period // 2} mod {N} = {x}")

    if x != 1 and x != N - 1:
        print("x ≠ 1 и x ≠ N-1, можно найти множители")

        p = gcd(x - 1, N)
        q = gcd(x + 1, N)

        print(f"gcd({x} - 1, {N}) = gcd({x - 1}, {N}) = {p}")
        print(f"gcd({x} + 1, {N}) = gcd({x + 1}, {N}) = {q}")

        if p > 1 and p < N:
            print(f"Найден множитель: p = {p}")
            print(f"Другой множитель: q = {N // p}")
            print(f"Проверка: {p} × {N // p} = {p * (N // p)}")
        elif q > 1 and q < N:
            print(f"Найден множитель: p = {q}")
            print(f"Другой множитель: q = {N // q}")
            print(f"Проверка: {q} × {N // q} = {q * (N // q)}")
    else:
        print(f"x = {x}, не подходит для разложения")
else:
    print("Период нечетный или не найден, метод не применим")
