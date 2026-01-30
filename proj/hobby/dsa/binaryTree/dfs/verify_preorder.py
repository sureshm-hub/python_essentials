from collections import deque

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        if "#" == preorder:
            return True # null is valid

        stack = deque() # child = 0, 1, 2
        nums = preorder.split(",")

        for i in range(len(nums)):
            num = nums[i]

            if "#" == num:
                if not stack:
                    return False # null needs a parent

                parent = stack.pop()
                parent += 1

                while parent == 2 and stack:
                    parent = stack.pop()
                    parent += 1

                if parent < 2:
                    stack.append(parent)

                if not stack:
                    return i  == len(nums) - 1 # did we use all elements
            else:
                stack.append(0)

        return not stack