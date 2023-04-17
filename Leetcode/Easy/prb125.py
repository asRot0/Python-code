s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
palindrome = ''.join(filter(str.isalnum, s)).lower()
print(palindrome == palindrome[::-1])


'''

import re
 
if __name__ == '__main__':
 
    input = "Welcome, User_12!!"
 
    s = re.sub(r'[^a-zA-Z0-9]', '', input)
    print(s)    # WelcomeUser12
'''