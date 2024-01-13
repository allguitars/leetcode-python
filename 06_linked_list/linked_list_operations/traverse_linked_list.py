from .list_node import ListNode
from typing import List


def traverse_linked_list(head: ListNode | None) -> List[ListNode]:
    if not head:
        return []

    current = head
    res = []

    while current:
        res.append(current.val)
        current = current.next

    return res
