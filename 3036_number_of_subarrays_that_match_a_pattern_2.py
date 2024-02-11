class Solution:
    
    def computeLPSArray(self,pattern, M, lps):
        length = 0
        lps[0] = 0
        i = 1
        while i < M:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1

    def KMPSearch(self,array, pattern):
        N = len(array)
        M = len(pattern)
        lps = [0]*M
        self.computeLPSArray(pattern, M, lps)

        i = j = 0
        matches = 0
        while i < N:
            if pattern[j] == array[i]:
                i += 1
                j += 1
            if j == M:
                matches += 1
                j = lps[j-1]
            elif i < N and pattern[j] != array[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return matches

    
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        full_pattern = []
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                full_pattern.append(1)
            elif nums[i+1] == nums[i]:
                full_pattern.append(0)
            else:
                full_pattern.append(-1)
        
        return self.KMPSearch(full_pattern, pattern)
