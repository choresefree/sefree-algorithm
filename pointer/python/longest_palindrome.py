class Solution:
    """
    题目: 最长回文子串
    思路: 双指针中心扩散
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def extend(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i, j = i - 1, j + 1
            return i + 1, j - 1

        beg, end = 0, 0
        for i in range(n):
            beg1, end1 = extend(i, i)
            beg2, end2 = extend(i, i + 1)
            if end1 - beg1 > end - beg:
                beg, end = beg1, end1
            if end2 - beg2 > end - beg:
                beg, end = beg2, end2

        return s[beg:end + 1]