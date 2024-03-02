class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root.val % 2: return False # test level 0
        d, lvl = [root], 0
        while True:
            d1 = [y for x in d for y in [x.left, x.right] if y]
            if not d1: break
            lvl += 1
            v1 = [x.val for x in d1]
            if lvl % 2:  # test odd level
                if (
                    any(x % 2 for x in v1)
                    or not v1[::-1] == sorted(v1)
                    or len(set(v1)) < len(v1)
                ):
                    return False
            else:  # test even level
                if (
                    any(not x % 2 for x in v1)
                    or not v1 == sorted(v1)
                    or len(set(v1)) < len(v1)
                ):
                    return False
            d = d1
        return True
