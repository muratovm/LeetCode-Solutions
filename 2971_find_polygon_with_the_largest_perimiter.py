import itertools

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefix_sum = [0]+list(itertools.accumulate(nums))
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < prefix_sum[i]:
                return prefix_sum[i+1]
        return -1
