#!/bin/python3


from main import Solution, ListNode

def createList(*l: int):
    l = list(l)
    head = ListNode(l[0],None)
    _head = head
    for i in l[1:]:
        _head.next = ListNode(i, None)
        _head = _head.next
    return head


if __name__ == "__main__":
    print(Solution().middleNode(createList(0,1,2)))
