# roman.py

def to_roman(decimal):
    if decimal == 0:
        return ""
    return "I" + to_roman(decimal - 1)
