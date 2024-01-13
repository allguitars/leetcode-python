'''
Time: O(n)
Space: O(n)

遞迴解法就是不斷拆分成較小目標

每一次的拆解分成：
1. head 跟
2. 剩下的 linked list
而較小目標就是將剩下的 linked list 反轉

較小目標解完後，回傳的就是反轉後的 tail。
接著就是 tail 指向原先的 head
再把原來的 head 指向 null 變成新的 tail
回傳 tail

'''

from linked_list_operations.list_node import ListNode
from linked_list_operations.build_linked_list import build_linked_list as build
from linked_list_operations.traverse_linked_list import traverse_linked_list as traverse


class Solution(object):
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        new_head = head  # 只是初始化，值為何不重要。

        # 除了 head 以外，如果還有剩下的部分 (head 後面還有)，就當成較小目標解決。
        # 這個較小目標就是將剩下的部分先反轉
        if head.next:
            # 接住子問題解決完送回來的尾巴
            # 較小目標解決後傳回來的，會是較小範圍 linked list 反轉後的尾巴！
            new_head = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        # 如果轉進來的 linked list 只有一個節點  則 new_head 就會是 head
        return new_head


head = build([1, 2, 3])
head = Solution().reverseList(head)

assert traverse(head) == [3, 2, 1]
print('Pass')
