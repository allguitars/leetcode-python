'''
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

NeetCode: https://youtu.be/gqXU1UyA8pk

#Medium
#SlidingWindow #HashTable #String

Similar Questions:
1004. Max Consecutive Ones III
2024. Maximize the Confusion of an Exam
2009. Minimum Number of Operations to Make Array Continuous
2213. Longest Substring of One Repeating Character
'''


class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        count = {}  # 記錄目前 window 裡面每個字母的出現次數
        res = 0

        # l, r 均從 0 開始
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)  # 在字典裡面記錄所有字母出現的次數

            # k 是允許被替換掉的字母數量，如果當前 window 長度減掉出現最多次的字母數量之後，
            # 仍然大於 k 的話，表示即使換掉 k 個字元，仍無法達到視窗內全部字元都相同的目標。
            # 那就表示目前視窗過大了，必須移動左指標。
            while (r - l + 1) - max(count.values()) > k:

                count[s[l]] -= 1     # 移動左指標之前，把左指標位置的字元從字典的數量中扣除
                l += 1               # 左指標右移

            res = max(res, r - l + 1)

        return res


solution = Solution()
assert solution.character_replacement('ABAB', 2) == 4
assert solution.character_replacement('AABABBA', 1) == 4


print('Pass')
