# https://leetcode.com/problems/wiggle-subsequence/description

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        lis, lds = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                lis = lds + 1
            elif nums[i - 1] > nums[i]:
                lds = lis + 1
        return max(lis, lds)