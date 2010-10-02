# roman.py

def to_roman(decimal):
    values = {
        10: "X",
         9: "IX",
         5: "V",
         4: "IV",
         0: "",
    }
    if decimal in values:
        return values[decimal]
    return to_roman(decimal - 1) + "I"
