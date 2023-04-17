num = 10
def is_palindrome(num):
    if num < 0:
        return False
    temp, reversed_num = num, 0
    print(reversed_num)
    while temp != 0:
        reversed_num = reversed_num * 10 + temp % 10
        print(reversed_num)
        temp //= 10
    #return num == reversed_num
    return True if(num == reversed_num) else False


#print('true') if (is_palindrome(num)) else print('false')
print(is_palindrome(num))


# def isPalindrome(self, x: int) -> bool:
#     if x < 0 or (
#             x > 0 and x % 10 == 0):  # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
#         return False
#
#     result = 0
#     while x > result:
#         result = result * 10 + x % 10
#         x = x // 10
#
#     return True if (x == result or x == result // 10) else False