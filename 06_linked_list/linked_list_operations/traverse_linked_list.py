from .list_node import ListNode


def traverse_linked_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
