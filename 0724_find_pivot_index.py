class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_prefix_sum = [0]
        right_prefix_sum = [0]

        for num in nums:
            left_prefix_sum.append(num+left_prefix_sum[-1])
        for num in nums[::-1]:
            right_prefix_sum.append(num+right_prefix_sum[-1])

        for i in range(len(left_prefix_sum)):
            opposite_index = len(right_prefix_sum)-2 - i
            if opposite_index <0: break
            if left_prefix_sum[i] == right_prefix_sum[opposite_index]:
                return i
        return -1
