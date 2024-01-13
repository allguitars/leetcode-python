'''
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/

Neetcode: https://youtu.be/G0_I-ZF0S38

Time: O(n)
Space: O(1)

Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Easy
#LinkedList #Recursion
'''

from linked_list_operations.list_node import ListNode
from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse


class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node, current = None, head

        while current:
            old_next = current.next    # backup
            current.next = prev_node   # reverse the direction

            # shift both pointers pointer by one step
            prev_node = current
            current = old_next

        # at the end the 'prev_node' pointer will point to the new head
        # and the 'current' pointer will point to None
        return prev_node


values = [1, 2, 3]
head = build(values)

head = Solution().reverseList(head)
assert traverse(head) == [3, 2, 1]

print('Pass')
