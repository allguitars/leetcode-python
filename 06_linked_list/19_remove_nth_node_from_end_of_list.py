'''
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

NeetCode: https://youtu.be/XVuQxVej6y8

#Medium
#LinkedList #TwoPointers
'''

from linked_list_operations.list_node import ListNode
from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        # 同步移動 left and right pointers
        while right:
            left = left.next
            right = right.next

        # remove the node
        left.next = left.next.next

        return dummy.next


head = build([1, 2, 3, 4, 5])
head = Solution().removeNthFromEnd(head, 2)
assert traverse(head) == [1, 2, 3, 5]

head = build([1, 2])
head = Solution().removeNthFromEnd(head, 1)
assert traverse(head) == [1]

head = build([1])
head = Solution().removeNthFromEnd(head, 1)
assert traverse(head) == []

print('Pass')
