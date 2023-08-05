from typing import List


class Solution:
    """
    题目: 接雨水
    链接: https://leetcode.cn/problems/trapping-rain-water/submissions/
    思路: 双指针, 当前盛水量 = min(前缀最大, 后缀最大) - 当前高度
    """
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        pre_max, suf_max = 0, 0
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max <= suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1

        return ans
