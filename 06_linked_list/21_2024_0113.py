from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse
from linked_list_operations.list_node import ListNode
from typing import Optional


class Solution:
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
