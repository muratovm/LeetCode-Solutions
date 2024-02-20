class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward_mult, backward_mult = [1], [1]
        for i in range(n):
            forward_mult.append(forward_mult[i] * nums[i])
            backward_mult.append(backward_mult[i] * nums[n-1-i])
        return [forward_mult[i] * backward_mult[n-1-i] for i in range(n)]
