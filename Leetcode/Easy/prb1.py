nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1]
table = {}


def find_num(nums):
    for i, val in enumerate(nums):
        if val in table:
            return table[val], i
        diff = target - val
        table[diff] = i


print(find_num(nums))
print(table)

'''
    for i, value in enumerate(nums):
        diff = target - value
        if diff in table:
            return table[diff], i
        table[value] = i
'''
