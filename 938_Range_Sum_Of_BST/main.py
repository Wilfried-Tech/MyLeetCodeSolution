#!/bin/python3

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return self.val+''


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if low <= root.val <= high:
            return self.rangeSumBST(root.left, low, high) + root.val + self.rangeSumBST(root.right, low, high)
        else:
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
