#!/bin/python3

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        return "ListNode{val: "+str(self.val)+", next: "+str(self.next)+"}"


# solution start 
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count,first =  0,head       
        while head is not None:
            count+=1
            head = head.next
        split_pos = int(count/2)
        while split_pos != 0:
            split_pos-=1
            first = first.next
        return first


