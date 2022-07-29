'''
46. Permutations
https://leetcode.com/problems/permutations/
NeetCode: https://youtu.be/s7AvT7cGdSo

#Backtracking #Array

宣告兩個陣列 res and current  每次到 base case 就把 current append 到 res
dfs():
base case: 如果 nums 的長度為零  將 current 加到 res
這個 decision tree 不是 binary  其分支數量由 nums 長度決定 -> for _ in range(len(nums))

Before calling dfs():
取出 nums 最前面的 item 並放到 current 最後

Call dfs()

After dfs():
還原 -> 從 current 最後面 pop  但是 <<<TRICK>>> 放到 nums 的最後面  而不是放回最前面
可以看成 nums 在 rotate: [1,2,3] -> [2,3,1]
'''


def permute(nums):
    res = []
    current = []

    def dfs():
        # IMPORTANT: remember NOT to modify 'current' array for the base case!!
        if len(nums) == 0:
            res.append(current[:])
            return

        for _ in range(len(nums)):           # -> nums=[1,2,3]
            # Always remove the first item
            item = nums.pop(0)               # -> item=1, nums=[2,3]
            current.append(item)             # current=[1]
            # 上面兩行可以簡寫為 current.append(nums.pop())  這樣就不需要額外的變數 item

            # pass down the way
            dfs()                            # nums=[2,3]

            # restore nums and current
            nums.append(item)                # nums=[2,3,1] -> 2 will then be removed for the next round
            current.pop()                    # []
            # 上面兩行可以簡寫為 nums.append(current.pop())

    dfs()
    return res


nums = [1, 2, 3]
print(permute(nums))
