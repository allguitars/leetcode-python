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


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

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
