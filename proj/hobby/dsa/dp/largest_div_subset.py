# https://leetcode.com/problems/largest-divisible-subset/description/
# dp + predecessor-chain
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        nums.sort()
        dp = [1] * n # dp[i] = length of best subset ending at i
        prev = [-1] * n # prev[i] = previous index in chain

        best_len = 1
        best_end = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                if dp[i] > best_len:
                    best_len = dp[i]
                    best_end = i

        # reconstruct
        res = []
        k = best_end
        while k != -1:
            res.append(nums[k])
            k = prev[k]

        res.reverse()
        return res