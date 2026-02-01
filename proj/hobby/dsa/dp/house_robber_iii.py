from typing import Optional, Dict, List

# https://leetcode.com/problems/house-robber-iii

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo: Dict[TreeNode, list] = {}
        take, skip = self.dfs(root, memo)
        max_val = max(take, skip)  # take, skip
        return max_val

    def dfs(self, node: TreeNode, memo: Dict[TreeNode, list]) -> list:
        if not node:
            return [0, 0] # take, skip

        if node in memo:
            return memo[node]

        L = self.dfs(node.left, memo)
        R = self.dfs(node.right, memo)

        take = node.val + L[1] + R[1] # skip  left & right child

        skip = max(L[0], L[1]) + max(R[0], R[1]) # choose skip or take on either child

        memo[node] = [take, skip]
        return memo[node]