'''
271. Encode and Decode Strings (LeetCode Premium)
https://leetcode.com/problems/encode-and-decode-strings/

NeetCode:
https://neetcode.io/problems/string-encode-and-decode
https://youtu.be/B1k_sxOSgv8

#Medium
#Array

這邊的範例所建立的 delimiter 會是每個字串的長度加一個 #
例如 'leetcode' 在 encode 之後會變成 7#leetcode 然後跟再其他字串合併成一整個字串
'''

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length

        return res


s = Solution()

encoded = s.encode(["neet", "code", "love", "you"])
print(encoded)  # 4#neet4#code4#love3#you
decoded = s.decode(encoded)
print(decoded)  # ['neet', 'code', 'love', 'you']

encoded = s.encode(["we", "say", ":", "yes"])
print(encoded)  # 2#we3#say1#:3#yes
decoded = s.decode(encoded)
print(decoded)  # ['we', 'say', ':', 'yes']
