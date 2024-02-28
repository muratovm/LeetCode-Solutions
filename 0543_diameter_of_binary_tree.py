# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def max_depth(node, depth):
            if node == None:
                return 0, 0

            if node.left == None and node.right == None:
                return 0, depth

            left_diameter, left_max_depth = max_depth(node.left, depth+1)
            right_diameter, right_max_depth = max_depth(node.right, depth+1)


            maximum_depth = max(left_max_depth, right_max_depth)
            maximum_diameter = max(left_diameter, right_diameter, left_max_depth+right_max_depth-(2*depth))

            return maximum_diameter, maximum_depth

        maximum_diameter, maximum_depth = max_depth(root,0)
        return maximum_diameter
