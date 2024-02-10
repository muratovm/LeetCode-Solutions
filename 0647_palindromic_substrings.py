import numpy as np

class Solution:

    def countSubstrings(self, s: str) -> int:

        n = len(s)
        dp = np.full((n,n), -1)

        def isPalindrome(i,j):
            print("called")
            if dp[i][j] >= 0:
                return dp[i][j]

            if j-i <= 0:
                return 1

            if s[i] == s[j] and isPalindrome(i+1,j-1):
                dp[i][j] = 1
            else:
                dp[i][j] = 0
            
            return dp[i][j]

        total = 0
        for i in range(n):
            for j in range(i+1,n):
                result = isPalindrome(i,j)
                total += int(result)
        return total + len(s)
