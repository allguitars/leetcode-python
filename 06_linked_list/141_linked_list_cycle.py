'''
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

NeetCode: https://youtu.be/gBTe7lFR3vc

Time: O(n)
Space: O(n) with a hash table or
        O(1) with a more complex algorithm called Floyd's Tortoise and Hare (龜兔賽跑)

#Easy
#LinkedList #TwoPointers #HashTable
'''

from linked_list_operations.list_node import ListNode
from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # 如果沒有閉環, fast 最終只會有兩個結果:
        # 1. 單數個節點時, fast 最後剛好停在最後一個節點, 此時 fast.next == None
        # 2. 單數個節點時, fast 最後剛好停在尾巴的下一個位置, 即 fast == None
        while fast and fast.next:
            # 當 fast 還沒抵達尾端
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        # list 有尾端
        return False


# 建立有閉環的 list
head = build([1, 2, 3, 4])

# 選擇第二個 node 當作接點
pos = head.next

# 找到 tail
current = head
while current.next:
    current = current.next

# tail node 接到 pos node
current.next = pos

# Test
assert Solution().hasCycle(head) == True

# 另一個沒有閉環的 list
head = build([1, 2, 3, 4, 5])
assert Solution().hasCycle(head) == False

print('Pass')
