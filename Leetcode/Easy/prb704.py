from typing import List

nums = [-1,0,3,5,9,12]
target = 9
# Output: 4
# Explanation: 9 exists in nums and its index i

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            midpoint = ((right - left) // 2) + left
            
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

val = Solution()
print(val.search(nums, target))