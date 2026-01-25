class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # num[0:i] -> first
        for i in range(1, n - 1): # i <= n - 2
            if num[0] == '0' and  i != 1:
                continue

            first = num[:i]

            for j in range (i + 1, n):
                if num[i] == '0' and j > i + 1:
                    continue

                second = num[i:j]
                if self._dfs(num, first, second, j):
                    return True

        return False

    def _dfs(self, num: str, first: str, second: str, s: int) -> bool:
        if s == len(num):
            return True

        third = str(int (first) + int (second))

        if not num.startswith(third, s):
            return False

        return self._dfs(num, second, third, s + len(third))

