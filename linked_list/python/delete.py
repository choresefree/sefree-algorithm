from typing import Optional
from link_list import ListNode


class Solution:
    """
    删除指定结点, 思路是构造一个假头结点head0, 这样可以完成的删除第一个结点
    """
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        head0 = ListNode(-1)
        head0.next = head

        p1, p2 = head0, head0.next
        while p2:
            if p2.val == val:
                p1.next = p2.next
                break
            p1, p2 = p1.next, p2.next

        return head0.next

