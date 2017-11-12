def alphabet_encode(number, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Converts an integer to an alphabet equivilent"""
    if not isinstance(number, (int, long)):
        raise TypeError("number must be an integer")

    if 0 <= number - 1 < len(alphabet):
        return alphabet[number - 1]

    base = ''
    while number != 0:
        number, r = divmod(number, len(alphabet))
        if r == 0:
            number = number - 1
        base = alphabet[r - 1] + base
    return base


def alphabet_decode(value, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    value.isalpha()
    value = value.upper()[::-1]
    number = 0
    for i in range(len(value)):
        number = ((len(alphabet) ** i) * (alphabet.index(value[i]) + 1)) + number
    return number
