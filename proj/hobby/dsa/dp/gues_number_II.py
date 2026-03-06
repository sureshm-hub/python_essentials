# https://leetcode.com/problems/guess-number-higher-or-lower-ii/?envType=problem-list-v2&envId=vorkm586
import functools

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(None)
        def dp(i: int, j: int) -> int:

            if i >= j:
                return 0

            # best = 10 ** 9
            # for k in range(i, j + 1):
            #     max_ik = dp(i, k - 1)
            #     max_kj = dp(k + 1, j)
            #     cost = max(max_ik, max_kj) + k
            #     best = min(best, cost)

            # return best

            # Generator comprehension
            return min (max(dp(i, k - 1), dp(k + 1, j)) + k
                        for k in range (i, j + 1))

        return dp(1, n)