# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recurse(self, node):
        if node == None:
            return 0, float('inf'), float('-inf')
        
        if node.left == None and node.right == None:
            return 0, node.val, node.val
        
        max_diff_l, left_min, left_max = self.recurse(node.left)
        max_diff_r, right_min, right_max = self.recurse(node.right)
        
        minimum = min(left_min, right_min, node.val)
        maximum =  max(left_max, right_max, node.val)
    
        max_diff = max(max_diff_l, max_diff_r, abs(node.val-minimum),abs(maximum-node.val))
        return max_diff, minimum, maximum
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root)[0]
