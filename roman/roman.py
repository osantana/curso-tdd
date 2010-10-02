# roman.py

def to_roman(decimal):
    if decimal == 9:
        return "IX"
    if decimal == 5:
        return "V"
    if decimal == 4:
        return "IV"
    if decimal == 0:
        return ""
    return to_roman(decimal - 1) + "I"
