# Input: s = "abacaba"
s = "abacaba"

# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.

new = set()
count = 1

for c in s:
    if c in new:
        count += 1
        new.clear()
    new.add(c)
print(count)