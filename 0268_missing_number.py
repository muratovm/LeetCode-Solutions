class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        expected = (n-1)*(n//2)
        if n%2 == 1: expected += n//2
        return expected - sum(nums)
