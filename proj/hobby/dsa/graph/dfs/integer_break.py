# https://leetcode.com/problems/integer-break/description

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        return self._dfs(n, memo)

    def _dfs(self, n: int, memo: dict[int, int]) -> int:
        if n == 1:
            return 0 # base case

        if n in memo:
            return memo[n]

        max_prod = 1  # n 1's
        for i in range(1, n):
            j = n - i
            max_j = self._dfs(j, memo)
            max_prod = max(max_prod, max(i * j, i * max_j))
        memo[n] = max_prod
        return max_prod
