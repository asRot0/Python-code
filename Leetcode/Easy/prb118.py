numRows = 5
res = [[1]]
for i in range(1, numRows):
    res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
    print(res)
# print(res)
print(res[:numRows])

'''
1210
0121
-----
1331 [add]
'''
# pascal = [[1]*(i+1) for i in range(5)]
# print(pascal)