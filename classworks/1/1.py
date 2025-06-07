def convert_to_q(a, n, q):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    a = int(str(a), n)
    res = ""
    while a != 0:
        if a % q > 9:
            res += alphabet[a % q - 10]
        else:
            res += str(a % q)
        a //= q
    return res[::-1]


print(convert_to_q(237, 8, 11))
