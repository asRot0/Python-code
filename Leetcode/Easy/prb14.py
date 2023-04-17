strs = ["dog","racecar","car"]
# Output: "fl"

# strs[:] = sorted(strs, key=len)
# print(strs)
#
# first, end = 0, len(strs[0])
# while first<end and strs[0][first] == strs[-1][first]:
#     first+=1
#
# print(strs[0][0:first])

size = len(strs)
strs.sort()
print(strs)

end = min(len(strs[0]), len(strs[size-1]))

i = 0
while (i < end and strs[0][i] == strs[size-1][i]):
    i+=1
print(strs[0][0: i])