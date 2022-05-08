# neetcode: https://youtu.be/9UtInBqnCgA
# Time: O(S + T)
# Space: O(S + T)

class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        # create a map for each string to store the count of characters

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)   # 0 is default if not in the map
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False

        return True


s = 'anagram'
t = 'nagaram'

print(Solution().isAnagram(s, t))
