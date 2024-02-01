class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        #goal minmize the difference by sorting
        nums.sort()
        num_groups, output = len(nums)//3, []
        
        #construct groups out of the sorted nums
        output = [nums[3*i: 3*(i+1)] for i in range(num_groups)]
        
        #check if a group contains a difference larger than k
        for group in output: 
            if group[2]-group[0] > k: return []
        return output
