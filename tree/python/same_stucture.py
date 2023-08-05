from tree.python.tree import TreeNode


class Solution:
    """
    题目: 输入两棵二叉树A和B, 判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
    思路: 逐个对比
    链接: https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof
    """
    def has_same_structure(self, A: TreeNode, B: TreeNode):
        if B is None:
            return True
        if A is None or A.val != B.val:
            return False

        return self.has_same_structure(A.left, B.left) and self.has_same_structure(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False
        queue = [A]
        while queue:
            node = queue.pop(0)
            if node:
                if self.has_same_structure(node, B):
                    return True
                queue.append(node.left)
                queue.append(node.right)

        return False