from math import comb
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            output.append([comb(i, j) for j in range(i+1)])
        return output
