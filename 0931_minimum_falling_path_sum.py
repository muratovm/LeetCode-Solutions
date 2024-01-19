class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        level_lenth = len(matrix[0])
        for l in range(1, len(matrix)):
            for i in range(level_lenth):
                options=[]
                upper_level = l-1
                if i-1 >= 0:
                    options.append(matrix[upper_level][i-1])
                options.append(matrix[upper_level][i])
                if i+1 < level_lenth:
                    options.append(matrix[upper_level][i+1])
                matrix[l][i] += min(options)
        return min(matrix[-1])
