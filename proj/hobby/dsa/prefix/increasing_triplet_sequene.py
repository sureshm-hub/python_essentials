from typing import List

#   https://leetcode.com/problems/increasing-triplet-subsequence
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        n = len(nums)
        min_left = [False] * n
        cur_min = nums[0]
        for i in range(n):
            if nums[i] > cur_min:
                min_left[i] = True
            else:
                cur_min = nums[i]

        cur_max = nums[n - 1]
        for i in range(n - 1, -1, -1):
            if nums[i] < cur_max:
                if min_left[i]:
                    return True # found an increasing triplet
            else:
                cur_max = nums[i]

        return False