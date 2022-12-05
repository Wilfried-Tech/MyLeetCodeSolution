#!/bin/python3

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return "ListNode{val: "+str(self.val)+", next: "+str(self.next)+"}"


# solution start
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = list()
        while head is not None:
            arr.append(head)
            head = head.next
        if len(arr) == 0:
            return None
        arr = arr[::2] + arr[1::2]
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        arr[-1].next = None
        return arr[0]

