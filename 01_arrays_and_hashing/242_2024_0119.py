
# 用額外的兩個 hashmap (dict)
# Time: O(s + t)
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # 若長度不一樣
            return False

        count_s, count_t = {}, {}
        # create the maps for both strings at once (兩個字串長度一樣)
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        # compare maps
        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False

        return True


# 把兩個字串都先排序，如果原先的字串是 anagrams，則排序後兩個字串應該要長得一樣。
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = Solution2()

assert s.isAnagram('anagram', 'nagaram') == True
assert s.isAnagram('rat', 'car') == False

print('Pass')
