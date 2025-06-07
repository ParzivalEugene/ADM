def find_divisors_by_length(n, length):
    divisors = []
    min_val = 10 ** (length - 1)
    max_val = 10**length - 1

    i = 1
    while i * i <= n:
        if n % i == 0:
            if min_val <= i <= max_val:
                divisors.append(i)

            if i != n // i:
                complement = n // i
                if min_val <= complement <= max_val:
                    divisors.append(complement)
        i += 1

    return sorted(divisors)


n = 123246369
print(f"Число: {n}")

three_digit_divisors = find_divisors_by_length(n, 3)
print(f"3-значные делители: {three_digit_divisors}")

seven_digit_divisors = find_divisors_by_length(n, 7)
print(f"7-значные делители: {seven_digit_divisors}")
