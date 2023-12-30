'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

NeetCode: https://youtu.be/wiGpQwVHdE0?si=6ljPdflpVIEGN6E4

#medium
#HashTable #String #SlidingWindow

Related problems:

159. Longest Substring with At Most Two Distinct Characters (M)
340. Longest Substring with At Most K Distinct Characters (M)
992. Subarrays with K Different Integers (H)

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # if we get to a duplicate char, we need to update the window and the set
            while s[r] in charSet:
                # remove the left char from our set
                charSet.remove(s[l])
                # shrink the window from the left
                l += 1

            # after removing all duplicate chars:
            # add the rightmost char to our set
            charSet.add(s[r])
            # at this point we are sure our substring/set does not have any duplicates
            # update our res, which stores the max length so far
            res = max(res, r-l+1)

        return res


solution = Solution()

assert solution.lengthOfLongestSubstring('abcaabcbb') == 3
assert solution.lengthOfLongestSubstring('bbbbb') == 1
assert solution.lengthOfLongestSubstring('pwwkew') == 3

print('All tests have passed.')
