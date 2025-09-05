def puissance(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("Only integers are allowed")

    if a == 0 and b < 0:
        raise ValueError("0 à une puissance négative est indéfini")

    result = 1

    for i in range(abs(b)):
        result *= a

    if b < 0:
        return 1 / result
    else:
        return result


