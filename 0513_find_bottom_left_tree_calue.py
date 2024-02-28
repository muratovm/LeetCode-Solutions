# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def recurse(node, depth):
            if node == None:
                return None, 0
            
            elif node.left == None and node.right == None:
                return node.val, depth
        
            else:
                new_depth = depth+1
                left_val, left_depth = recurse(node.left, new_depth)
                right_val, right_depth = recurse(node.right, new_depth)
                
                if right_depth > left_depth:
                    return right_val, right_depth
                else:
                    return left_val, left_depth
        return recurse(root, 0)[0]
