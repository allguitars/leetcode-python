'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

NeetCode: https://youtu.be/vzdNOK2oB2E

#Medium
#Array #HashTable #String #Sorting

方法一：
把所以字串都先排序，假設有輸入陣列裡面有 m 個字串，每個字串有 n 的字元，則全部排序完會花費 O(m x n log n)

方法二：
Time: O(m x n)
m 為輸入字串數量, n 為每個字串的平均長度

利用一個 map
key 是字母的組成
value 是一個 list, 只要字串擁有該 key 所描述的字母組成，就 append 到這個 list 裡面。

使用collections.defaultdict是實現這個功能的一個非常好的方式。
如果您嘗試查找的key不存在  defaultdict允許您提供一個預設的工廠函數用於自動產生那個key的值
在這個情況下  我們將使用list作為工廠函數以創建空列表

from collections import defaultdict

# 創建一個defaultdict  指定list作為預設工廠函數
dict_with_default_list = defaultdict(list)

# 現在  當您訪問不存在的key時  將返回一個新的空list
print(dict_with_default_list['some_key'])  # 輸出: []

# 您也可以像正常的dict一樣添加key-value pairs
dict_with_default_list['existing_key'] = ['item']

# 打印帶有存在和不存在的key的dictionary
print(dict_with_default_list['existing_key'])  # 輸出: ['item']
print(dict_with_default_list['other_key'])     # 輸出: []
'''

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # 傳入 list 作為一個 factory function

        for s in strs:
            # 建立字母組成統計的陣列，它是一個長度固定為 26 的陣列。
            # 每一個位置屬於一個字母，index 0 數於 a, index 1 數於 b, index 數於 c, and so on
            # 每個位置的初始值為 0
            count = [0] * 26

            for c in s:
                # 計算每個字母的相對 ASCII 值，當作 index
                # 然後該位置的 count 加一
                count[ord(c) - ord('a')] += 1

            # 在 Dict 中建立"字母組成"與字串本身的關聯
            # list 不能 Dict 的 key，所以必須先轉成 tuple
            res[tuple(count)].append(s)

        return res.values()


s = Solution()

print(s.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
print(s.groupAnagrams(['']))
print(s.groupAnagrams(['a']))
