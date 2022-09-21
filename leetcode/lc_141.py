# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
        
    if not head.next:
        return False
        
    over_1 = head.next
    over_2 = head.next.next
        
    while True:
        if over_1 == None or over_2 == None:
            return False
        if over_1 == over_2:
            return True
        over_1 = over_1.next
        over_2 = over_2.next
        if over_2:
            over_2 = over_2.next
