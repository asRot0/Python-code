from itertools import zip_longest
pattern = "abba"
s = "dog cat cat dog"

s = s.split()

print(len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern, s))))
print(list(zip_longest(pattern,s)))