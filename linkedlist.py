from typing import Optional

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data: int = data
        self.next: Optional[ListNode] = next_node
