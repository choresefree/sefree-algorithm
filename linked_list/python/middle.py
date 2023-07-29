from typing import Optional
from link_list import ListNode


class Solution1:
    """
    题目1: 给你单链表的头结点head, 请你找出并返回链表的中间结点
    题目链接: https://leetcode.cn/problems/middle-of-the-linked-list
    如果是1->2->3, 返回2; 如果是1->2->3->4, 返回3
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        # 如果1->2->3->4想返回2,可以建一个head0,head0.next=head即可,slow从head0出发即可
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow
