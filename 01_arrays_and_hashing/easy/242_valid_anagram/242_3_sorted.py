# 242: Valid anagram
# neetcode: https://youtu.be/9UtInBqnCgA
# 這個解法的目標是不需要額外的記憶體
# Time: sorting 可能會是 O(N logN)  但是否假設排序不需要額外的記憶體  可以跟面試官討論
# Space: O(1) -> no need for extra memory

# 如果是 anagram string 則排序之後  兩者應該會呈現一樣的字串

class Solution(object):
    def isAnagram(self, s, t):

        return sorted(s) == sorted(t)


s = 'anagram'
t = 'nagaram'

print(Solution().isAnagram(s, t))

# Time: O(S + T)
# Space: O(S + T)
