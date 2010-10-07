
def roman(n):
    if n < 1:
        return ""

    conversion_table = (
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    )

    res = ""
    while n:
        for i, r in conversion_table:
            if n >= i:
                res += r
                n -= i
                break
    return res


