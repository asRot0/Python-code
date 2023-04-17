# using binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x

        low, high = 1, x
        while low<=high:
            mid = (low+high) // 2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                low = mid +1
            else:
                high = mid -1
        return high


ob1 = Solution()
print(ob1.mySqrt(4))



'''
def sqrt(n):
	if n < 2:
		return n
	low, high = 1, n
	while low <= high:
		mid = (low + high) // 2
		if mid * mid == n:
			return mid
		elif mid * mid < n:
			low = mid + 1
		else:
			high = mid - 1
	return high


n=4
print(sqrt(n))
'''