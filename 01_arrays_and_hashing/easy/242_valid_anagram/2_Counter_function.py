# neetcode: https://youtu.be/9UtInBqnCgA
# 使用內建的函式 Counter()  可以用來快速建立 count map

from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):

        return Counter(s) == Counter(t)


s = 'anagram'
t = 'nagaram'

print(Solution().isAnagram(s, t))

# Time: O(S + T)
# Space: O(S + T)
