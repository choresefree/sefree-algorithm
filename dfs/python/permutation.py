from typing import List


class Solution:
    """
    输入一个字符串, 打印出该字符串中字符的所有排列。
    输入: s = "abc"
    输出: ["abc","acb","bac","bca","cab","cba"]
    """

    def permutation(self, s: str) -> List[str]:
        if s == "":
            return [""]

        ans = []
        for i, c1 in enumerate(s):
            for c2 in self.permutation(s[:i] + s[i + 1:]):
                ans.append(c1 + c2)

        return list(set(ans))
