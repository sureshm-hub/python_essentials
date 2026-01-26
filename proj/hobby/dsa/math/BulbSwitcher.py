from math import sqrt, floor

# https://leetcode.com/problems/bulb-switcher/description
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Don't need to simulate.
        #
        # Each bulb is toggled number of factors of its index. Only perfect squares have odd divisors and all other
        # bulb's get toggled even number of times remaining in OFF state.
        # example: bulb 4: 1, 2, 4 -> ON
        return len(range(floor(sqrt(n))))