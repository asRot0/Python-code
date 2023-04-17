s = ["h", "e", "l", "l", "o"]

len_s = len(s)
for i in range(0, len_s // 2):
    s[i], s[len_s - 1 - i] = s[len_s - 1 - i], s[i]

print(s)
# with one line
s[:] = s[::-1]
'''
s[:] = s[::-1] is required NOT s = s[::-1] because you have to edit the 
list inplace. Under the hood, s[:] = is editing the actual memory 
bytes s points to, and s = points the variable name s to other bytes 
in the memory. 
'''
