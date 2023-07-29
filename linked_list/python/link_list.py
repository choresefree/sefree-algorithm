class ListNode:
    """
    链表结点定义
    """

    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def print(self):
        p = self
        s = []
        while p:
            s.append(str(p.val))
            p = p.next
        print("->".join(s))
