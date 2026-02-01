from typing import List
# https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:

        result = [0] * (n + 1)

        for i in range(n + 1):
            ans = i
            count = 0
            while ans > 0:
                if ans & 1:
                    count += 1
                ans = ans >> 1

            result[i] = count

        return result