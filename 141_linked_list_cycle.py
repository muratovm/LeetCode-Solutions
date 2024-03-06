# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize a set to keep track of visited nodes
        seen = set()

        # Traverse the linked list until reaching the end (None)
        while head:

            # If the current node is already in the set, it means there is a cycle
            if head in seen:
                return True

            # Add the current node to the set and move to the next node
            seen.add(head)
            head = head.next

        # If the loop completes without finding a cycle, return False
        return False
