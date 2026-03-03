# https://leetcode.com/problems/sum-of-two-integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # mask for 32 bits
        max_int = 0x7FFFFFFF
        carry = 0
        res = 0

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = 1 if (a_bit + b_bit + carry) >= 2 else 0

            if cur_bit:
                res |= (1 << i)


        # handle negative numbers (2's complement)
        if res > max_int:
            res = ~(res ^ mask)

        return res