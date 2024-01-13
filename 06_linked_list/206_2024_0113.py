from linked_list_operations.list_node import ListNode
from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse


class Solution(object):
    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            # back up the next
            next = current.next
            # revers link
            current.next = prev
            # shift both pointers
            prev = current
            current = next

        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if not head:
            return None

        new_head = head

        if head.next:
            new_head = self.reverseListRecursive(head.next)
            head.next.next = head

        head.next = None
        return new_head


head = build([1, 2, 3])
head = Solution().reverseListIterative(head)
assert traverse(head) == [3, 2, 1]

head = build([1, 2, 3])
head = Solution().reverseListRecursive(head)
assert traverse(head) == [3, 2, 1]


print('Pass')
