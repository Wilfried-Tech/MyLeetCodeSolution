#!/bin/python3

# Definition for a binary tree node.
from inspect import getabsfile
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        pass

    def getBase(self, l: List[TreeNode]) -> List[int|TreeNode]:
        if len([0 for v in l if type(v) == TreeNode]) != 0:
            for v in l:
                if v is TreeNode:
                    index = l.index(v)
                    l = l[:index] + self.getBase([v.left]) + self.getBase([v.right])+ l[index+1:]
            return l
        return l
        