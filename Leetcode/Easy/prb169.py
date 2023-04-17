nums = [2,2,1,1,1,2,2]
# Output: 2

print(max(set(nums), key=nums.count))

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
'''