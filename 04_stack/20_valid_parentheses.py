# 20. Valid Parentheses
# neetcode: https://youtu.be/WTzjTskDFMg

# Time: O(n)
# Space: O(n) -> the size of the stack could be up to the size of the input


from fileinput import close


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in close_to_open:        # if we see a closing one, check the stack
                if stack and stack[-1] == close_to_open[c]:   # if stack is not empty and the top matches
                    stack.pop()
                else:
                    return False
            else:  # if we see an open one
                stack.append(c)

        # we can only return true if the stack is empty
        return True if not stack else False


s1 = '()'
s2 = '()[]{}'
s3 = '(]'

print(Solution().isValid(s1))
