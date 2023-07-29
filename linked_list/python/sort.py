from typing import Optional
from link_list import ListNode


class Solution:
    """
    题目1: 重排链表
    链接: https://leetcode.cn/problems/reorder-list
    Do not return anything, modify head in-place instead.
    """

    def show(self, head):
        ss = []
        p = head
        while p:
            ss.append(str(p.val))
            p = p.next
        print("->".join(ss))

    def get_middle(self, head):
        """
        获得右半部的起始node, 同时断开左右的连接
        """
        head0 = ListNode(-1)
        head0.next = head
        slow, fast = head0, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        tmp = slow.next
        slow.next = None
        return tmp

    def reverse(self, head):
        """
        逆转链表,返回新链表的首部
        """
        if not head:
            return head
        p1, p2 = head, head.next
        while p2:
            tmp1, tmp2 = p2, p2.next
            p2.next = p1
            p1, p2 = tmp1, tmp2
        head.next = None
        return p1

    def reorderList1(self, head: Optional[ListNode]) -> None:
        """
        虽然成功了,但是不是原地置换
        """
        if not head.next:
            return head
        right = self.get_middle(head)
        right = self.reverse(right)
        self.show(right)

        left = head
        self.show(left)

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        原地置换
        """
        if not head.next:
            return head
        right = self.get_middle(head)
        right = self.reverse(right)
        self.show(right)

        left = head.next
        self.show(left)

        p = head

        while right and left:
            tmp_left, tmp_right = left.next, right.next
            p.next = right
            p.next.next = left
            p = p.next.next
            left, right = tmp_left, tmp_right

        if right:
            p.next = right

        return head

