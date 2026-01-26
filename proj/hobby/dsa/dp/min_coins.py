from typing import List

# https://leetcode.com/problems/coin-change
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        min_coins = [INF] * (amount + 1)
        min_coins[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0 and min_coins[i-c] != INF:
                    min_coins[i] = min(min_coins[i], min_coins[i - c] + 1)

        return -1 if min_coins[amount] == INF else min_coins[amount]