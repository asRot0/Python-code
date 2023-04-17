from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums2 = Counter(nums2)
        for i in nums1:
            check = nums2.get(i)
            if check!= None and check>0:
                nums2[i]-=1
                result.append(i)
        return result





nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

# Output: [4,9]
# Explanation: [9,4] is also accepted.

obj = Solution()
print(obj.intersect(nums1,nums2))
