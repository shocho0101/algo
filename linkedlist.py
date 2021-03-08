from typing import Optional

class ListNode:
    def __init__(self, data=0, next_node=None, prev_node=None):
        self.data: int = data
        self.next: Optional[ListNode] = next_node
        self.prev: Optional[ListNode] = prev_node
