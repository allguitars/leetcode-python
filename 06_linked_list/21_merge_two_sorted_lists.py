# 21. Merge Two Sorted Lists
# neetcode: https://youtu.be/XIdigk956u0

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 新的 list 由一個 dummy node 開始，目的是為了避免 edge case -> 插入到一個空的 list
# 先產生一個 dummy node 是常見的技巧


class Solution(object):
    def mergeTwoLists(self, list1, list2):  # list1 跟 list2 都是 ListNode，指著 list head。
        dummy = ListNode()
        tail = dummy

        while list1 and list2:  # 當兩個 list 都不是空的，或尚未移動到尾巴。
            if list1.val < list2.val:
                tail.next = list1   # 將比較小的 node 接在 tail 後面
                list1 = list1.next  # 移動 pointer 以進行下一輪比較
            else:
                tail.next = list2
                list2 = list2.next

            # update the tail pointer
            tail = tail.next

        # 可能還有一個 list 具有一個或多個 node 未處理
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next
