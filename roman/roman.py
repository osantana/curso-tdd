# roman.py

def to_roman(decimal):
    values = (
        (1000, "M"),
        ( 900, "CM"),
        ( 500, "D"),
        ( 400, "CD"),
        ( 100, "C"),
        (  90, "XC"),
        (  50, "L"),
        (  40, "XL"),
        (  10, "X"),
        (   9, "IX"),
        (   5, "V"),
        (   4, "IV"),
        (   1, "I"),
    )

    for d, v in values:
        if decimal == d:
            return v

        if decimal > d:
            return to_roman(d) + to_roman(decimal - d)

    return ""
