'''
125. Valid Palindrome
neetcode: https://youtu.be/jJXJ16kPFWg

Time: O(n)
Space: O(1)

We do not want to use extra memory, which means solving it
without creating a new version of string.
We will use pointers.
Use ASCII code to determine alphanumeric

#Easy
#TwoPointers
'''


def is_palindrome(s):
    '''
    :type s: str
    :rtype: bool
    '''
    left, right = 0, len(s)-1

    while left < right:
        # make sure the chars to compare are both alphanumeric
        while left < right and not is_alphanumeric(s[left]):
            left += 1
        while left < right and not is_alphanumeric(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left, right = left+1, right-1  # keep moving towards the center

    return True


def is_alphanumeric(c):
    '''
    write our own function to determine alphanumeric
    ord function is to get the ASCII value of the character
    '''
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


s1 = 'A man, a plan, a canal: Panama'
s2 = 'race a car'
s3 = ' '

print(is_palindrome(s1))
