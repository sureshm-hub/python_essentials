# https://leetcode.com/problems/super-pow
# a ** (10x+d) ≡ (a ** x )** 10  * a ** d (mod 1337)
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        ans = 1

        for i in b:
            ans = pow(ans, 10, MOD) * pow(a, i, MOD)

        return ans % MOD