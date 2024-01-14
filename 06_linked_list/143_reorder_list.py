'''
143. Reorder List
https://leetcode.com/problems/reorder-list/description/

NeetCode: https://youtu.be/S5bfdUTrKLM

Time: O(n)
Space: O(1)

#Medium
#LinkedList #TwoPointers #Stack #Recursion
'''

from linked_list_operations.list_node import ListNode
from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 利用 slow 跟 fast pointer 來決定區分兩個 lists 的地方
        slow = head
        fast = head.next

        while fast and fast.next:
            # fast 還沒觸及最後一個節點或是 null
            slow = slow.next
            fast = fast.next.next  # fast pointer 移動速度是 slow pointer 的兩倍

        # 此時 slow 的下個節點會是第二段的頭
        second = slow.next
        # 且 slow 是第一段的尾巴  即最後一個節點  故其 next 指向 null
        slow.next = None

        # 開始反轉第二段
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 反轉第二段後  開始交錯結合兩段 lists
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


s = Solution()
head = build([1, 2, 3, 4])
s.reorderList(head)
assert traverse(head) == [1, 4, 2, 3]

head = build([1, 2, 3, 4, 5])
s.reorderList(head)
assert traverse(head) == [1, 5, 2, 4, 3]

print('Pass')
