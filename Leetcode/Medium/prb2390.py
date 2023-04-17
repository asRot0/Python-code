from collections import deque

# Input: s = "leet**cod*e"
# Output: "lecoe"

class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for c in s:
            if c == '*':
                stack and stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


obj = Solution()
s = "leet**cod*e"
print(obj.removeStars(s))
