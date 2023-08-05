from typing import Optional
from tree.python.tree import TreeNode


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 1
        queue = [(root, 1)]
        while queue:
            for _ in range(len(queue)):
                node, idx = queue.pop(0)
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
            if len(queue) > 1:
                _, left = queue[0]
                _, right = queue[-1]
                ans = max(right - left + 1, ans)

        return ans