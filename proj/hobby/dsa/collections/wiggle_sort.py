from typing import List

# https://leetcode.com/problems/wiggle-sort-ii
#
# straight splice won't If you just take the second half and interleave it forward with the first half,
# duplicates can sit next to each other and break the < > < > pattern.
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        arr = sorted(nums)
        mid = (n - 1) // 2 # floor(n/2)  -> floor division won't work for even lengthed arrays

        for i, j in zip(range(0, n, 2), range(mid, -1, -1)):
            nums[i] = arr[j]

        for i, j in zip(range (1, n, 2), range(n - 1, mid, -1)):
            nums[i] = arr[j]