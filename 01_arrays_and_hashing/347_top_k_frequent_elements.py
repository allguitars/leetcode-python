'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

NeetCode: https://youtu.be/YPTqKIgVk-k

#Medium
#Array #HashTable #DivideAndConquer #Sorting 
#Heap #PriorityQueue #BucketSort #Counting #QuickSort
'''

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # index stands for the appearance count
        # each element is a list containing all the numbers that appear i times, where i is
        # the index of the array
        freq = [[] for i in range(len(nums) + 1)]  # 2-D array

        # build the count map
        # key: number
        # value: count
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # build the freq array
        # 陣列的位置 / index 代表數字出現在的次數
        # 將出現相同次數的數字放在同一個位置，故每個位置都是一個 list。
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # 從陣列最右邊開始抓 k 個數字（因為是 top k）
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


s = Solution()

assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert s.topKFrequent([1], 1) == [1]

# 題目有說明 It is guaranteed that the answer is unique.
# 所以不會出現下面這種 test case: 1 出現三次，2 跟 5 出現兩次，當要抓出現頻率最高的兩個數字時（k=2）
# 則可能有兩種答案 -> [1, 2] 與 [1, 5]
print(s.topKFrequent([1, 1, 1, 2, 2, 3, 5, 5], 2))

# 但是如果搭配 k=3 就是合理的 test case，因為 [1, 2, 5] 是唯一解
print(s.topKFrequent([1, 1, 1, 2, 2, 3, 5, 5], 3))  # [1,2,5]

print('Pass')
