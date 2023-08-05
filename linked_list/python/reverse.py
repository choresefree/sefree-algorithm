from typing import Optional
from link_list import ListNode


class Solution:
    """
    题目1: 逆转链表
    """

    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        p1, p2 = head, head.next
        while p2:
            tmp1, tmp2 = p2, p2.next
            # 不能用tmp1 = p1.next，因为p1.next发生了变化
            p2.next = p1
            p1, p2 = tmp1, tmp2
        head.next = None
        return p1


if __name__ == "__main__":
    head0 = ListNode(-1)
    p = head0
    for num in [1, 2, 3, 4, 5]:
        node = ListNode(num)
        p.next = node
        p = node
    head = head0.next
    s = Solution()
    print(s.reverseList(head).print())

