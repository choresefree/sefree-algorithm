from typing import List


class Solution:
    """
    给定一个整数数组 temperatures, 表示每天的温度, 返回一个数组 answer, 其中 answer[i] 是指对于第 i 天,
    下一个更高温度出现在几天后。如果气温在这之后都不会升高, 请在该位置用 0 来代替。
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for j, temp in enumerate(temperatures):
            if not stack or temp <= temperatures[stack[-1]]:
                stack.append(j)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    i = stack.pop(-1)
                    ans[i] = j - i
                stack.append(j)

        return ans
