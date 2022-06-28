import unittest
# Listas de los numeros romanos
def intToRoman(num):
  
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
     "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
     "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
    "VI", "VII", "VIII", "IX"]

    miles = m[num // 1000]
    cientos = c[(num % 1000) // 100]
    decenas = x[(num % 100) // 10]
    unos = i[num % 10]
  
    result = (miles + cientos + decenas + unos)
  
    return result

