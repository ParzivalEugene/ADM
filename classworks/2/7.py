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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print("Задача 7: Разделить 1 на 7 по модулю 8")
print()

a = 7
m = 8

print("Нужно найти x такое, что 7x ≡ 1 (mod 8)")
print("Это эквивалентно нахождению обратного элемента 7 по модулю 8")
print()


gcd_val = gcd(a, m)
print(f"gcd({a}, {m}) = {gcd_val}")

if gcd_val == 1:
    print("Поскольку gcd(7, 8) = 1, обратный элемент существует")
    print()

    inverse = mod_inverse(a, m)
    if inverse is not None:
        print(f"Обратный элемент 7 по модулю 8: {inverse}")

        check = (a * inverse) % m
        print(f"Проверка: 7 × {inverse} = {a * inverse} ≡ {check} (mod 8)")

    print(f"\nОтвет: 1/7 ≡ {inverse} (mod 8)")

    print("\nВычисления расширенным алгоритмом Евклида:")
    print("Нужно найти x, y такие, что 7x + 8y = 1")

    gcd_val, x, y = extended_gcd(a, m)
    print(f"7 × {x} + 8 × {y} = {gcd_val}")
    print(f"Значит, 7 × {x} ≡ 1 (mod 8)")

    x_mod = (x % m + m) % m
    print(f"x ≡ {x} ≡ {x_mod} (mod 8)")

    print("\nПроверка всех остатков от 0 до 7:")
    for i in range(m):
        product = (a * i) % m
        if product == 1:
            print(f"7 × {i} ≡ {product} (mod 8) ✓")
        else:
            print(f"7 × {i} ≡ {product} (mod 8)")

else:
    print(f"Поскольку gcd(7, 8) = {gcd_val} ≠ 1, обратный элемент не существует")
    print("Деление 1 на 7 по модулю 8 невозможно")
