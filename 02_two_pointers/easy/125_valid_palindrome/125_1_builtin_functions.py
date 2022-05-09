# 125. Valid Palindrome
# neetcode: https://youtu.be/jJXJ16kPFWg

# Use python built-in functions

class Solution(object):
    def isPalindrome(self, s):
        '''
        :type s: str
        :rtype: bool
        '''
        new_string = ''

        # we want to ignore the non-alphanumeric characters and ignore cases
        for c in s:
            if c.isalnum():  # is alphanumeric?
                new_string += c.lower()  # conver to lowercase

        return new_string == new_string[::-1]


s1 = 'A man, a plan, a canal: Panama'
s2 = 'race a car'
s3 = ' '

print(Solution().isPalindrome(s1))
