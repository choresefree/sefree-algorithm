class Solution:
    """
    题目: 把数字翻译成字符串
    链接: https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
    """
    def translateNum(self, num: int) -> int:
        num = str(num)
        n = len(num)
        if n <= 1:
            return 1
        dp = [0] * n  # dp[i]表示[0:i](闭区间)的子问题
        dp[0], dp[1] = 1, 2 if "10" <= num[:2] <= "25" else 1

        for i in range(2, n):
            dp[i] = dp[i - 1]
            if "10" <= num[i - 1:i + 1] <= "25":
                dp[i] += dp[i - 2]

        return dp[-1]
