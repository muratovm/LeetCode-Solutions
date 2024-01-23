import numpy as np

class Solution:
    
    def __init__(self):
        self.answers = None
        self.string = None
        self.pattern = None
        
    def recurse(self, i,j):
        #if at the end of both string and pattern, return true
        if i == len(self.string) and j == len(self.pattern):
            return 1
        
        #if inside the string and pattern, check sub problem solution
        elif i < len(self.string) and j < len(self.pattern):
            if self.answers[i][j] != -1:
                return self.answers[i][j]
            
        #if outside string or pattern
        else:
            #if string is empty and lookahead
            if i == len(self.string) and j <= len(self.pattern)-2:
                if self.pattern[j+1] == "*":
                    return self.recurse(i, j+2)
                else:
                    return 0
            #if string is empty and there's no lookahead
            else:
                return 0
        
        #if reached end of pattern or string
        if i == len(self.string) or j == len(self.pattern):
            self.answers[i][j] = len(self.pattern) - j == len(self.string) - i
            return self.answers[i][j]
        
        #lookahead by one
        if len(self.pattern) - j >= 2 and self.pattern[j+1] == "*":
            #skip the asterisks if there's no match or no wildcard
            if self.string[i] != self.pattern[j] and self.pattern[j] != ".":
                self.answers[i][j] = self.recurse(i, j+2)
                return self.answers[i][j]

            #if there's a match continue discard the asterisk and increment the string or keep it as is
            self.answers[i][j] = self.recurse(i+1, j) or self.recurse(i+1,j+2) or self.recurse(i, j+2)
            return self.answers[i][j]
        
        # match on wildcard
        elif self.pattern[j] == ".":
            self.answers[i][j] = self.recurse(i+1, j+1)
            return self.answers[i][j]
        else:
            self.answers[i][j] = self.pattern[j] == self.string[i] and self.recurse(i+1, j+1)
            return self.answers[i][j]
        
    
    def isMatch(self, s: str, p: str) -> bool:
        self.string = s
        self.pattern = p
        self.answers = np.full((len(s),len(p)), -1)
        self.recurse(0,0)
        
        result = self.answers[0][0]
        if result == -1:
            return False
        return result
