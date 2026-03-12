import functools
from typing import List

# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @functools.cache
        def memo(nums: tuple[int, ...], target: int) -> int:
            if target == 0:
                return 1
            if target < 0:
                return -1

            count = 0
            for n in nums:
                sub = memo(nums, target - n)
                if sub > 0:
                    count += sub

            return count
        return memo(tuple(nums), target)