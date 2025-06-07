def last_nonzero_digit_factorial(n):
    if n < 2:
        return 1

    factors_2 = 0
    factors_5 = 0

    temp = n
    while temp > 0:
        temp //= 2
        factors_2 += temp

    temp = n
    while temp > 0:
        temp //= 5
        factors_5 += temp

    result = 1

    for i in range(1, n + 1):
        temp = i

        while temp % 2 == 0:
            temp //= 2
        while temp % 5 == 0:
            temp //= 5
        result = (result * temp) % 10

    extra_twos = factors_2 - factors_5
    for _ in range(extra_twos):
        result = (result * 2) % 10

    return result


def last_nonzero_digit_factorial_table(n):
    if n < 2:
        return 1

    table = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

    if n < 10:
        return table[n]

    result = 1
    for i in range(1, min(n + 1, 1000)):
        temp = i
        while temp % 10 == 0:
            temp //= 10
        result = (result * (temp % 10)) % 10
        if result == 0:
            result = 1

    return result


print("Задача 2: Последняя ненулевая цифра факториала")


n1 = 11
result1 = last_nonzero_digit_factorial(n1)
print(f"Последняя ненулевая цифра {n1}! = {result1}")


factorial_11 = 1
for i in range(1, 12):
    factorial_11 *= i
print(f"11! = {factorial_11}")
print(f"Последняя ненулевая цифра 11! (проверка): {str(factorial_11).rstrip('0')[-1]}")


n2 = 101
result2 = last_nonzero_digit_factorial(n2)
print(f"Последняя ненулевая цифра {n2}! = {result2}")
