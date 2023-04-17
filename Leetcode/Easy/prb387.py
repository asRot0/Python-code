from collections import Counter
s = "leetcode"
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ch, val in Counter(s).items():
            if val==1:
                return s.index(ch)
        return -1