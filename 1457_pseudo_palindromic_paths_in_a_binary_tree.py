from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def determine_palindrome(path):
            encountered_odd = 0
            for key in path:
                encountered_odd += path[key] % 2
            return encountered_odd <= 1

        #problem requires DFS + Counter
        stack = [(root, defaultdict(int))]
        total = 0
        
        while stack:
            node, path = stack.pop()
            if node:
                new_path = path.copy()
                new_path[node.val] += 1
                if node.left == None and node.right == None:
                    total += determine_palindrome(new_path)
                else:
                    stack.append((node.left, new_path))
                    stack.append((node.right, new_path))
        return total
