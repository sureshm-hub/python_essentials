from collections import Counter
from typing import List

# Time: O(M+N) Space: O(Min(M, N))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        # Time: O(MXN) Space: O(MAX(M, N))
        # used = [0] * len(nums2)
        # for i in range(len(nums1)):
        #     n1 = nums1[i]
        #     for j in range(len(nums2)):
        #         n2 = nums2[j]
        #         if n1 == n2 and used[j] == 0:
        #             ans.append(n2)
        #             used[j] = 1
        #             break
        # return ans
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        counts = Counter(nums1)
        for num in nums2:
            if counts[num] > 0:
                ans.append(num)
                counts[num] -= 1
        return ans