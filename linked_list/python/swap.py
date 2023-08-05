from typing import Optional
from link_list import ListNode


class Solution:
    """
    题目: 两两交换链表中的节点
    链接: https://leetcode.cn/problems/swap-nodes-in-pairs/description
    思路: 增加假头结点, 窗口为3进行交换, 每次行进两步
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head0 = ListNode(-1, head)
        p1 = head0
        # p1, p2 = head0, head0.next
        while p1.next and p1.next.next:
            p2 = p1.next
            p3 = p2.next
            p2.next = p3.next
            p1.next = p3
            p3.next = p2
            p1, p2 = p2, p2.next

        return head0.next
