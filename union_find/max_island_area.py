from typing import List


class Solution:
    """
    题目: 岛屿的最大面积
    """

    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        """
        思路: 并查集
        """
        row, col = len(grid), len(grid[0])
        root = [0] * (row * col)

        for i in range(row):
            for j in range(col):
                idx = i * col + j
                root[idx] = idx

        def find(x):
            r = root[x]
            if r != x:
                root[x] = find(r)
            return root[x]

        def merge(x1, x2):
            root1, root2 = find(x1), find(x2)
            if root1 != root2:
                # 这里是root1和root2, 而不是x1和x2
                root[root1] = root2

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    idx = i * col + j
                    if i > 0 and grid[i - 1][j] == 1:
                        merge(idx, idx - col)
                    if j > 0 and grid[i][j - 1] == 1:
                        merge(idx, idx - 1)

        area = dict()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    idx = i * col + j
                    r = find(idx)
                    if r in area:
                        area[r] += 1
                    else:
                        area[r] = 1

        if area:
            return max(area.values())
        else:
            return 0

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        """
        思路: dfs
        """
        ans = 0
        visits = set()
        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            if i in (-1, row) or j in (-1, col) or grid[i][j] == 0 or (i, j) in visits:
                return 0
            visits.add((i, j))
            # 记得也要向上向左传播
            return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)

        for i in range(row):
            for j in range(col):
                ans = max(ans, dfs(i, j))

        return ans
