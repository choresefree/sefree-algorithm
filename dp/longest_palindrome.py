class Solution:
    """
    题目: 最长回文子串
    思路: 动态规划
    """

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        # dp[i][j]表示s[i:j+1]是否是回文子串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(1, n):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = True

        left, right = 0, 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                if dp[i][j] and j - i > right - left:
                    left, right = i, j

        return s[left:right + 1]
