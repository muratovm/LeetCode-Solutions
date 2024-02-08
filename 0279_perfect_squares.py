import math
class Solution:

    def __init__(self):
        self.solutions = {0:0}

    def numSquares(self, n: int) -> int:
        if n in self.solutions:
            return self.solutions[n]

        if int(sqrt(n))**2 == n:
            return 1

        options = [i**2  for i in range(max(1,int(sqrt(n))//2),int(sqrt(n))+1)]
        results = []
        for option in options:
            results.append(1 + self.numSquares(n-option))

        self.solutions[n] = min(results)
        return self.solutions[n]
