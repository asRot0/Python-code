nums = [3,2,2,3]
val = 3
# Output: 2, nums = [2,2,_,_]

print(id(nums))
nums[:] = [x for x in nums if x!=val]
print(nums)
print(len(nums))
print(id(nums))