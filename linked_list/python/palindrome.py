from linked_list.python.link_list import ListNode


class Solution:
    def show(self, head):
        ss = []
        p = head
        while p:
            ss.append(str(p.val))
            p = p.next
        print("->".join(ss))

    def get_middle(self, head):
        # 加入头头结点确保右边的起始正确
        head0 = ListNode(-1, head)
        slow, fast, count = head0, head, 0
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow.next

    def reverse(self, head):
        if not head or not head.next:
            return head
        p1, p2 = head, head.next
        while p2:
            tmp1, tmp2 = p2, p2.next
            p2.next = p1
            p1, p2 = tmp1, tmp2
        head.next = None
        return p1

    def isPalindrome(self, head: ListNode) -> bool:
        left, right = head, self.reverse(self.get_middle(head))
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
