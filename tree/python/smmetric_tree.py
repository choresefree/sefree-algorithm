from tree.python.tree import TreeNode


class Solution:
    """
    题目: 判断是否是对称树
    """

    def order(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return self.order(root1.left, root2.right) and self.order(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.order(root, root)
