from typing import List


class Solution:
    """
    题目: 假设把某股票的价格按照时间先后顺序存储在数组中, 请问买卖该股票一次可能获得的最大利润是多少?
    链接: https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof/
    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        动态规划, dp[i]表示子问题[0:i]的最大利润, 实施记录此前最小值(如果不这样每一步依然要遍历前面所有获得最小值)
        """
        n = len(prices)
        if n < 2:
            return 0
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            if prices[i] >= prices[i - 1]:
                dp[i] = max(dp[i], dp[i - 1])
            if prices[i] >= min_price:
                dp[i] = max(dp[i], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max(dp)
