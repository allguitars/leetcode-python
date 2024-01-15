'''
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

NeetCode: https://youtu.be/q5a5OiGbT6Q

#Hard
#LinkedList #DivideAndConquer #Heap #PriorityQueue #MergeSort
'''

from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse
from linked_list_operations.list_node import ListNode
from typing import Optional, List


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge cases
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []
            # Pick two lists to merge each time
            # lists[0] 跟 lists[1] merge, lists[2] 跟 lists[3] merge, and so on...
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # 如果 lists 陣列中只剩下一個 list，則 i 為 0 時，i+1 會超出範圍。
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                # 解子問題
                merged_lists.append(self.mergeTwoLists(l1, l2))

            # for loop 跳出後，merged_lists 中約有原 lists 中一半的串列。
            # 將其覆寫回 lists -> 故 while loop 每次都會讓 lists 減半，直到只剩一個 list 即跳出。
            lists = merged_lists

        # 只剩下一個 list
        return lists[0]

    # Subproblem from another LeetCode problem
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next


s = Solution()

head1 = build([1, 4, 5])
head2 = build([1, 3, 4])
head3 = build([2, 6])
merged_list = s.mergeKLists([head1, head2, head3])
assert traverse(merged_list) == [1, 1, 2, 3, 4, 4, 5, 6]

merged_list = s.mergeKLists([])
assert traverse(merged_list) == []

merged_list = s.mergeKLists([[]])
assert traverse(merged_list) == []

print('Pass')
