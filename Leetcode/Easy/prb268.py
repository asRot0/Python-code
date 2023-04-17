nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all
# numbers are in the range [0,3]. 2 is the missing number in the range
# since it does not appear in nums.


li = set(range(0, len(nums)+1))
print(li)

# print(li.difference(nums).pop())
print(next(iter(li.difference(nums))))

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1))//2 - sum(nums)        
'''
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x ^ y, list(range(len(nums)+1)) + nums)
'''