'''
LeetCode: 90. Subsets II
https://leetcode.com/problems/subsets-ii/

NeetCode: https://youtu.be/Vn2v6ajA7U0

#Medium 
#Backtracking #Array #BitManipulation
'''


def subsetsWithDup(nums):
    # 題目沒有說明 input 是排序好的  故需要先排序
    nums.sort()

    # output 為 list of lists -> 故使用 res & curr 兩個 list
    res = []
    curr = []

    # recursion: decision tree 的每一層都代表 input 的一個 position i
    # 每次遞迴呼叫都將 i 推進一個位置
    def dfs(i):
        # base case: tree 的底部代表 i 已經到達最後個位置，不能再推進了。
        if i == len(nums):
            res.append(curr[:])
            return

        # all subsets that include nums[i]

        curr.append(nums[i])
        dfs(i+1)

        # restore
        curr.pop()

        # all subsets that do not include nums[i]

        # 會發生相同 subset 的情況在於：
        # 兩個具有相同 parent 的節點，當"右邊"節點在加入下一個數字時，剛好跟"左邊節點未加入"下一個數字的情況相同。
        # 更簡單的判斷方式是 input array (排序後) 具有重複的數字  例如 [1,2,2,3]  就會發生這種情況
        # 解決辦法是：
        # 右邊節點"跳過這個已經用過的數字"  如果還是相同的數字  就繼續跳過  直到出現不同數字  才開始加入該數字

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            # 如果下一個數字仍是相同的數字，就持續忽略，直到數字不一樣為止。但要注意是否超過邊界！
            i += 1

        dfs(i+1)

    dfs(0)

    return res


nums = [1, 2, 2]
print(subsetsWithDup(nums))
