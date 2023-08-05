class Solution:
    """
    题目: 请从字符串中找出一个最长的不包含重复字符的子字符串,计算该最长子字符串的长度。
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        思路: 动态规划
        """
        if not s:
            return 0
        n = len(s)
        dp = [1] * len(s)
        for i in range(1, n):
            c = s[i]
            j = i - 1
            while j >= 0 and s[j] != c:
                j -= 1
            if i - j <= dp[i - 1]:
                dp[i] = i - j
            else:
                dp[i] = dp[i - 1] + 1
        return max(dp)

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        思路: 滑动窗口
        """
        window, ans = [], 0
        for c in s:
            while c in window:
                window.pop(0)
            window.append(c)
            ans = max(len(window), ans)

        return ans
