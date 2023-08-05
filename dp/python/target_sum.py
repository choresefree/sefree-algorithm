from functools import cache
from typing import List


class Solution:
    """
    题目1: 目标和
    链接: https://leetcode.cn/problems/target-sum/description
    思路:
        dp[i][j]表示从[0, i]个物品中选择重量为j的方案数
        如果nums[i]小于j, 说明索引i的数字不可选, dp[i][j] = dp[i-1][j];
        否则索引i的数字可选, 会分支, dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]].
        退出条件, 索引为-1时, 说明无物可选, 如果此时j==0, 返回1, 否则返回0
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        根据上述思路, dfs的实现
        """
        # 正整数和 p, 负整数和 sum - p, p - (sum - p) = target, p = (target + sum) / 2
        num_sum = sum(nums)
        if (target + num_sum) % 2 == 1:
            return 0
        target = (target + num_sum) // 2

        @cache
        def dfs(i, weight):
            """
            从[0, i-1]物体中选择weight大小的方案个数
            """
            if i < 0:
                return 1 if weight == 0 else 0
            if nums[i] > weight:
                return dfs(i - 1, weight)
            return dfs(i - 1, weight) + dfs(i - 1, weight - nums[i])

        return dfs(len(nums) - 1, target)

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target % 2 == 1 or target < 0:
            return 0
        target //= 2

        row, col = len(nums) + 1, target + 1
        # 初始化dp数组, dp[i][j]表示从前i个数字中选和为j组合方案的个数
        dp = [[0] * col for _ in range(row)]
        # 正确
        dp[0][0] = 1
        # # 错误, dp[3][0]代表从物体1,2,3中和为0的选择，方案数是8
        # for i in range(row):
        #     dp[i][0] = 1
        # for j in range(1, col):
        #     dp[0][j] = 0
        # dp推理
        for i in range(1, row):
            for j in range(col):
                weight = j - nums[i - 1]
                dp[i][j] += dp[i - 1][j]  # 不选该物
                if weight >= 0:
                    dp[i][j] += dp[i - 1][weight]  # 选择怪物
        for row in dp:
            print(row)

        return dp[-1][-1]