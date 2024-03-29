'''
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

NeetCode: https://youtu.be/XIdigk956u0

#Easy
#LinkedList #Recursion
'''

from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse
from linked_list_operations.list_node import ListNode
from typing import Optional

# 新的 list 由一個 dummy node 開始，目的是為了避免 edge case -> 插入到一個空的 list
# 先產生一個 dummy node 是常見的技巧


class Solution:
    # list1 跟 list2 都是 ListNode，指著 list head。
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:  # 當兩個 list 都不是空的，或尚未移動到尾巴。
            if list1.val < list2.val:
                tail.next = list1   # 將比較小的 node 接在 tail 後面
                list1 = list1.next  # 移動 pointer 以進行下一輪比較
            else:
                tail.next = list2
                list2 = list2.next

            # update the tail pointer
            tail = tail.next

        # 可能還有一個 list 具有一個或多個剩餘節點
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next


head1 = build([1, 2, 4])
head2 = build([1, 3, 4])
new_head = Solution().mergeTwoLists(head1, head2)
assert traverse(new_head) == [1, 1, 2, 3, 4, 4]

head1 = build([])
head2 = build([])
new_head = Solution().mergeTwoLists(head1, head2)
assert traverse(new_head) == []

head1 = build([])
head2 = build([0])
new_head = Solution().mergeTwoLists(head1, head2)
assert traverse(new_head) == [0]

print('Pass')
