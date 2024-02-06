class Solution:
    
    def __init__(self):
        self.n = None

    def recurse(self, left, right, net, string):
        if left == self.n and right == self.n and net == 0:
            return [string]

        options = []
        #add right parenthesis
        if net > 0:
            results = self.recurse(left, right+1, net-1, string+")")
            options.extend(results)

        #add left parenthesis
        if net < self.n and left < self.n:
            results = self.recurse(left+1, right, net+1, string+"(")
            options.extend(results)
        return options

    def generateParenthesis(self, n):
        self.n = n
        return self.recurse(1,0,1,"(")
