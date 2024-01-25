import numpy as np
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        shape = (len(text1), len(text2))
        dp = np.zeros(shape, dtype=int)
        i,j = 0,0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if text1[i] == text2[j]:
                    if i-1 < 0 or j-1 < 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    term1,term2 = 0,0
                    if i-1 >= 0:
                        term1 = dp[i-1][j]
                    if j-1 >= 0:
                        term2 = dp[i][j-1]
                    
                    dp[i][j] = max(term1,term2)
        return dp[-1][-1]
