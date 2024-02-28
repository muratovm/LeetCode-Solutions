# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #p and q roots exists and have the same value
        if p and q and p.val == q.val:
            #recursive call on the left and right subtrees
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        #both trees terminate at None in the same palce
        elif p == None and q == None:
            return True
        #if neither are true then there is a mismatch
        else:
            return False
