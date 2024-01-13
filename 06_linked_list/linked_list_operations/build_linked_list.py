from .list_node import ListNode
from typing import List


def build_linked_list(values: List[int]) -> ListNode:
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head
