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


def find_all_invertible_elements(n):
    invertible = []
    for a in range(1, n):
        if gcd(a, n) == 1:
            inverse = mod_inverse(a, n)
            invertible.append((a, inverse))
    return invertible


def verify_inverse(a, inv, n):
    return (a * inv) % n == 1


n = 12

print(f"Задача 6: Найти все обратимые элементы относительно умножения по модулю {n}")
print()


print(f"Числа от 1 до {n - 1}, взаимно простые с {n}:")
coprime_numbers = []
for i in range(1, n):
    if gcd(i, n) == 1:
        coprime_numbers.append(i)
        print(f"gcd({i}, {n}) = {gcd(i, n)}")

print(f"\nВзаимно простые числа с {n}: {coprime_numbers}")
print()


invertible_elements = find_all_invertible_elements(n)

print("Обратимые элементы и их обратные:")
print("a\ta^(-1)\ta * a^(-1) mod 12")
print("-" * 30)

for a, inv in invertible_elements:
    product = (a * inv) % n
    print(f"{a}\t{inv}\t{a} * {inv} = {a * inv} ≡ {product} (mod {n})")

print(
    f"\nВсе обратимые элементы по модулю {n}: {[a for a, inv in invertible_elements]}"
)


print("\nПроверка:")
for a, inv in invertible_elements:
    is_correct = verify_inverse(a, inv, n)
    print(f"{a} * {inv} ≡ {(a * inv) % n} (mod {n}) - {'✓' if is_correct else '✗'}")


print("\nДополнительная информация:")
print(f"Количество обратимых элементов: {len(invertible_elements)}")
print(f"Это равно φ({n}) = {len(coprime_numbers)}")


print(f"\nРазложение {n} на простые множители: {n} = 2² × 3")
print(f"φ({n}) = φ(2² × 3) = φ(4) × φ(3) = (4 - 2) × (3 - 1) = 2 × 2 = 4")


print(f"\nГруппа обратимых элементов (Z/{n}Z)* = {{1, 5, 7, 11}}")
print("Эта группа изоморфна Z/2Z × Z/2Z (группа Клейна)")
