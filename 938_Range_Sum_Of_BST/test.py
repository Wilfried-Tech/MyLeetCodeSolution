#!/bin/python3

from typing import List
from main import Solution, TreeNode


def treeNodeToArr(nodes: List[TreeNode]) -> List[int]:
    childs = []
    siblings = []
    for node in nodes:
        if node is not None:
            siblings.append(node.val)
            if node.left != None or node.right != None:
                childs.append(node.left)
                childs.append(node.right)
        else:
            siblings.append(None)
    if len([v for v in childs if type(v) == TreeNode]) != 0:
        return [*siblings, *treeNodeToArr(childs)]
    else:
        return [*siblings, *childs]


if __name__ == "__main__":
    print(treeNodeToArr([TreeNode(10, TreeNode(5, TreeNode(3, None, None),
          TreeNode(7, None, None)), TreeNode(15, None, TreeNode(18)))]))
    print([10, 5, 15, 3, 7, None, 18])
