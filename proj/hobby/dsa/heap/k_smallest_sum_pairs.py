from collections import namedtuple
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        heap = []

        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while len(result) < k and heap:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
