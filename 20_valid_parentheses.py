class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:  # Early return for odd-length strings
            return False
        
        matching = {"(": ")", "[": "]", "{": "}"}
        stack = []
        
        for char in s:
            if char in matching:
                stack.append(char)
            else:
                if not stack or char != matching[stack.pop()]:
                    return False

        return len(stack) == 0
