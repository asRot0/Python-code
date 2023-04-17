s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

symbol = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
s = s.replace('IV', 'IIII')\
    .replace('IX', 'vIIII')\
    .replace('XL', 'XXXX')\
    .replace('XC', 'LXXXX')\
    .replace('CD', 'CCCC')\
    .replace('CM', 'DCCCC')

print(sum(map(symbol.get, s)))