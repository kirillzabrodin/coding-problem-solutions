import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    initial_node = head
    count = 1
    while initial_node.next != None:
        initial_node = initial_node.next
        count += 1

    for i in range(int(count/2)):
        head = head.next

    return head
