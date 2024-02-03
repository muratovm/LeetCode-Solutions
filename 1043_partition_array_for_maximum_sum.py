import numpy as np

class Solution:

    def __init__(self):
        self.n = None
        self.arr = None
        self.k = None
        self.solutions = {}

    def recurse(self, start):
        if start in self.solutions:
            return self.solutions[start]
        
        options = []
        n = self.n - start 
        for l in range(1,min(self.k+1,n+1)):
            current_chunk = max(self.arr[start:start+l])*l
            options.append(current_chunk + self.recurse(start+l))
        
        biggest = max(options)
        self.solutions[start] = biggest
        return biggest

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.arr = arr
        self.n = len(arr)
        self.k = k

        self.solutions[self.n] = 0
        self.solutions[self.n-1] = arr[-1]

        return self.recurse(0)
