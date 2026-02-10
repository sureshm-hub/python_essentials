#https://leetcode.com/problems/reverse-string
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        last = len(s) - 1
        for i in range(0, len(s)//2):
            s[i], s[last-i] = s[last-i], s[i]
