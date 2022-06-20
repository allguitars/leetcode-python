'''
347. Top K Frequent Elements

neetcode: https://youtu.be/YPTqKIgVk-k

Time:
- O(n) with this solution
- O(k * log n) with the heap sort solution

#Amazon
'''


class Solution:
    def top_k_frequent(self, nums, k):
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # create the count hashma
        # this takes O(n) time
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # default: 0

        print(count)

        # create the bucket
        # [[], [3], [2], [1]]  <- 1 put in index 3 because it appears three times
        # this also takes O(n) time
        for num, count in count.items():
            freq[count].append(num)

        print(freq)

        # create the result
        # this also takes O(n) time
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res


nums = [1, 1, 1, 2, 3, 5, 5]
k = 2

print(Solution().top_k_frequent(nums, k))  # [1, 5]
