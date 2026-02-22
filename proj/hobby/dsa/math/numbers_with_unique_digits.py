class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        count = 10 # n <= 1 uniq digit numbers
        start = 9

        for i in range(2, n+1):
            next = 9 - i + 2 # n <= 8 so next won't be -ve
            start *= next

            count += start

        return count