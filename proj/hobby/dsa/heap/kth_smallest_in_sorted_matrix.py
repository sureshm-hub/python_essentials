from typing import List
import heapq

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = []
        N = len(matrix)
        for i in range(min(N, k)):
            heapq.heappush(q, (matrix[i][0], i, 0))

        while k != 1:
            min_val = heapq.heappop(q)
            k -= 1
            x = min_val[1]
            y = min_val[2]
            if y + 1 < N:
                heapq.heappush(q, (matrix[x][y + 1], x, y + 1))
        min_val = heapq.heappop(q)
        return min_val[0]