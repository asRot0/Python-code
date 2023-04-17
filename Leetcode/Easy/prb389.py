s = "a"
t = "aa"

# print('"{}"'.format(*set(t).difference(set(s))))

for i in s:
    t = t.replace(i, '', 1)
print(t)
