# https://leetcode.com/problems/odd-even-linked-list
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = temp_odd = ListNode(); even = temp_even = ListNode(); cur = head
        idx = 1
        while cur:
            if idx % 2 == 1:
                temp_odd.next = ListNode(cur.val)
                temp_odd = temp_odd.next
            else:
                temp_even.next = ListNode(cur.val)
                temp_even = temp_even.next
            cur = cur.next
            idx += 1

        temp_odd.next = even.next
        return odd.next




