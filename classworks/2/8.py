def solve_remainder_problem():
    print("Задача 8: Число a даёт остаток 5 при делении на 10.")
    print("Может ли оно давать остаток 11 при делении на 22?")
    print()

    print("Дано: a ≡ 5 (mod 10)")
    print("Вопрос: может ли a ≡ 11 (mod 22)?")
    print()

    print("Если a ≡ 5 (mod 10), то a = 10k + 5 для некоторого целого k")
    print()

    print("Проверим, может ли 10k + 5 ≡ 11 (mod 22)")
    print("10k + 5 ≡ 11 (mod 22)")
    print("10k ≡ 6 (mod 22)")
    print()

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_val = gcd(10, 22)
    print(f"НОД(10, 22) = {gcd_val}")

    print(f"Проверим, делится ли 6 на {gcd_val}: 6 % {gcd_val} = {6 % gcd_val}")

    if 6 % gcd_val == 0:
        print(
            f"Поскольку 6 делится на {gcd_val}, уравнение 10k ≡ 6 (mod 22) имеет решение"
        )

        print()
        print("Упростим уравнение, разделив на НОД:")
        print("5k ≡ 3 (mod 11)")

        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            gcd_val, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd_val, x, y

        def mod_inverse(a, m):
            gcd_val, x, y = extended_gcd(a, m)
            if gcd_val != 1:
                return None
            return (x % m + m) % m

        inv_5 = mod_inverse(5, 11)
        if inv_5 is not None:
            k_solution = (3 * inv_5) % 11
            print(f"Обратный элемент 5 по модулю 11: {inv_5}")
            print(f"k ≡ 3 × {inv_5} ≡ {k_solution} (mod 11)")

            print()
            print("Найдем несколько значений a:")
            for i in range(3):
                k = k_solution + 11 * i
                a = 10 * k + 5
                remainder_10 = a % 10
                remainder_22 = a % 22
                print(
                    f"k = {k}: a = {a}, a mod 10 = {remainder_10}, a mod 22 = {remainder_22}"
                )

        print()
        print("Ответ: ДА, число может давать остаток 11 при делении на 22")

    else:
        print(
            f"Поскольку 6 не делится на {gcd_val}, уравнение 10k ≡ 6 (mod 22) не имеет решения"
        )
        print("Ответ: НЕТ, число не может давать остаток 11 при делении на 22")

    print()
    print("Дополнительная проверка через систему сравнений:")
    print("Система: a ≡ 5 (mod 10) и a ≡ 11 (mod 22)")

    print("НОД(10, 22) = 2")
    print("Проверим совместность: 5 ≡ 11 (mod 2)")
    print(f"5 mod 2 = {5 % 2}, 11 mod 2 = {11 % 2}")

    if 5 % 2 == 11 % 2:
        print("Остатки совпадают по модулю НОД, система совместна")
    else:
        print("Остатки не совпадают по модулю НОД, система несовместна")


solve_remainder_problem()
