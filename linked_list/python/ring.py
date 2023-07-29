from typing import Optional
from link_list import ListNode


class Solution1:
    """
    题目1: 给定一个链表的头节点head, 判断链表是否有环
    题目链接: https://leetcode.cn/problems/linked-list-cycle
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        最好思路: 快慢指针, 快慢均从head开始, 快每次两步, 慢每次一步, 二者相遇则说明链表有环
        两个指针相遇的时候, 慢指针必然没有走完整个链表, 相对速度,二者速度差v=1, 极限情况fast在slow的前一位, t = (ring_length - 1) / v
        """
        slow, fast = head, head
        # while slow and slow.next and fast and fast.next:
        # 退出的情况是非环,这种情况下只需有关注fast,因为他会比slow更早的为none
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True

        return False


class Solution2:
    """
    题目2: 给定一个链表的头节点head,返回链表开始入环的第一个节点。 如果链表无环,则返回None
    题目链接：https://leetcode.cn/problems/linked-list-cycle/discussion
    最差思路：逐个遍历
    """

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        快慢指针相遇后,头结点和快指针分别v=1行进,最终会在入口相遇
        """
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                while head != fast:
                    head, fast = head.next, fast.next
                return fast
