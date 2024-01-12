# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def distance(self, ancestors, value):
        if len(ancestors) < 1:
            return 0
        return max([abs(ancestors[i] - value) for i in range(len(ancestors))])
    
    def recurse(self, ancestor_values, node):    
        if node == None:
            return 0
        
        if node.left == None and node.right == None:
            return self.distance(ancestor_values, node.val)
        
        new_ancestor_values = ancestor_values + [node.val]
        left_distances = self.recurse(new_ancestor_values, node.left)
        right_distances = self.recurse(new_ancestor_values, node.right)
        current_distance = self.distance(ancestor_values, node.val)
        return max(left_distances,right_distances,current_distance )
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.recurse([], root)
