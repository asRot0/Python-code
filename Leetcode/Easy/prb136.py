import functools
li = [4,1,2,1,2]

print(functools.reduce(lambda a, b: a^b, li))