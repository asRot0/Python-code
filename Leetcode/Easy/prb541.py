# class Solution:
#     def reverseStr(self, s: str, k: int) -> str:
#         for i in range(0,len(s),2*k):
#             if(i+k<len(s)):
#                 s=s[0:i]+s[i:i+k][::-1]+s[i+k:]
#             else:
#                 s=s[0:i]+s[i:i+k][::-1]
#         return s
#


'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        if k>n:
            return s[-1::-1]
        l, r, rem = 0, k, n
        s=s[k-1::-1]+s[k:]
        l+=2*k
        r=l+k-1
        rem=n-l
        while l<=n:
            if k>rem:
                s=s[:l]+s[-1:l-1:-1]
                return s
            if rem>=k and rem<2*k:
                s=s[:l]+s[r:l-1:-1]+s[r+1:]
                return s
            s=s[:l]+s[r:l-1:-1]+s[r+1:]
            l+=2*k
            r=l+k-1
            rem=n-l
        return s
'''

s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
k = 39

if(len(s)<=k):
    s = s[::-1]
else:
    for i in range(0, len(s), 2*k):
        s=s[0:i]+s[i:i+k][::-1]+s[i+k:]
print(s)