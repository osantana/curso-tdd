# roman.py

def to_roman(decimal):
    values = {
        40: "XL",
        10: "X",
         9: "IX",
         5: "V",
         4: "IV",
         1: "I",
    }

    if decimal in values:
        return values[decimal]

    for d in (10, 9, 5, 4, 1):
        if decimal > d:
            return to_roman(d) + to_roman(decimal - d)

    return ""
