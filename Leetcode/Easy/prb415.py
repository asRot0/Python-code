class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def strtoint(num):
            result = 0
            for n in num:
                result = result * 10 + ord(n) - ord('0')
            return result

        return str(strtoint(num1) + strtoint(num2))


num1 = "11"
num2 = "123"
# Output: "134"

val = Solution()
print(val.addStrings(num1, num2))
