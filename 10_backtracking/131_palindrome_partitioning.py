'''
131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

NeetCode: https://youtu.be/3jvWodd7ht0
Back to Back SWE: https://youtu.be/4ykBXGbonlA
'''


def partition(s):
    def isPali(s):
        return s == s[::-1]

    res = []
    part = []

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return

        # 'aab'
        # 若 i=0 -> j in range(0,3) -> j=0~2 -> j+1 當作 slicing 尾端
        # 取一個字：s[i:j+1] -> s[0:1]
        # 取兩個字：s[0:2]
        # 取三個字：s[0:3]  j 最大為 2  故到這裡停止
        for j in range(i, len(s)):
            slice = s[i:j+1]

            if isPali(slice):
                part.append(slice)
                dfs(j+1)
                part.pop()
    dfs(0)
    return res


s = 'aab'
print(partition(s))

s = 'a'
print(partition(s))
