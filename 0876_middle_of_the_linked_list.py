# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def length(self, node):
        if node == None:
            return 0
        return 1 + self.length(node.next)
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = self.length(head) // 2
        
        i = 0
        while i < middle:
            i+= 1
            head = head.next
        return head
