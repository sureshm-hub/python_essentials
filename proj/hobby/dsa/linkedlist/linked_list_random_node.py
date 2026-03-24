# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        index = random.randint(0, 10000)
        temp = self.head
        size = 0
        while temp and index > 0:
            temp = temp.next
            index -= 1
            size += 1

        if temp:
            return temp.val

        index = index % size

        temp = self.head
        while temp and index > 0:
            temp = temp.next
            index -= 1

        return temp.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()